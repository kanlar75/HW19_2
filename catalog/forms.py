from django import forms

from catalog.models import Product, Version
from django.forms.models import BaseInlineFormSet


class FormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ContactForm(FormMixin, forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(label='Сообщение', widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))


class ProductForm(FormMixin, forms.ModelForm):
    stop_list = [
        'КАЗИНО', 'КРИПТОВАЛЮТА', 'КРИПТА', 'БИРЖА', 'ДЕШЕВО', 'БЕСПЛАТНО',
        'ОБМАН', 'ПОЛИЦИЯ', 'РАДАР'
    ]

    class Meta:
        model = Product
        exclude = ('user_owner',)

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')
        for word in ProductForm.stop_list:
            if word in cleaned_data.upper():
                raise forms.ValidationError('Запрещенные слова в названии продукта')
            else:
                continue

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')
        for word in ProductForm.stop_list:
            if word in cleaned_data.upper():
                raise forms.ValidationError('Запрещенные слова в описании продукта')
            else:
                continue

        return cleaned_data


class VersionForm(FormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'


class VersionFormSet(forms.BaseInlineFormSet):

    def clean(self):
        super().clean()
        direct_ancestor_count = 0
        for form in self.forms:
            if form['is_direct_ancestor'].data:
                direct_ancestor_count += 1
                if direct_ancestor_count > 1:
                    raise forms.ValidationError('Активной может быть только одна версия!')
