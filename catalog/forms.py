from django import forms

from catalog.models import Product, Version


class FormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


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
