from django import forms
from app.rent.models import Apartment, Price


class AddApartmentForm(forms.ModelForm):

    start_price = forms.FloatField()

    def clean_name(self):
        name = self.cleaned_data['name']

        if len(name) < 2:
            raise forms.ValidationError(
                'Nome do apartamento deve ter no mínimo dois caracteres.'
            )

        if Apartment.objects.filter(name=name).exists():
            raise forms.ValidationError(
                'Apartamento com nome "%s" já cadastrado.',
                params=name
            )
        return name

    def save(self):
        apartment = super(AddApartmentForm, self).save(commit=True)
        Price(
            value=self.cleaned_data['start_price'],
            apartment=apartment
        ).save()
        return apartment

    class Meta:
        model = Apartment
        fields = ['name']
