from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):
    stop_list = ['КАЗИНО', 'КРИПТОВАЛЮТА', 'КРИПТА', 'БИРЖА', 'ДЕШЕВО', 'БЕСПЛАТНО', 'ОБМАН', 'ПОЛИЦИЯ', 'РАДАР']

    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data.get('name')

        if cleaned_data.upper() in ProductForm.stop_list:
            raise forms.ValidationError('Ошибка, связанная с именем продукта')

        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data.get('description')

        if cleaned_data.upper() in ProductForm.stop_list:
            raise forms.ValidationError('Ошибка, связанная с описанием продукта')

        return cleaned_data
