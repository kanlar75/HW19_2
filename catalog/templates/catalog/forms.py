from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    stop_list = [
        'КАЗИНО', 'КРИПТОВАЛЮТА', 'КРИПТА', 'БИРЖА', 'ДЕШЕВО', 'БЕСПЛАТНО',
        'ОБМАН', 'ПОЛИЦИЯ', 'РАДАР'
    ]

    class Meta:
        model = Product
        fields = '__all__'

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
