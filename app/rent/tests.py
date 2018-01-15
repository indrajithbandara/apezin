from app.base.tests import BaseTestCase, required_field_validator
from app.rent.models import Apartment, Price
from app.rent.forms import AddApartmentForm
from django import forms


class ApartmentTestCase(BaseTestCase):
    """
    TestCase to Apartment Model
    """

    def test_add(self):
        """
        Try to add an apartment
        and see it in a list
        """

        form_alpha = AddApartmentForm({
            'name': 'AP01',
            'start_price': 350.2
        })

        self.assertTrue(form_alpha.is_valid(), form_alpha.errors)
        apartment_alpha = form_alpha.save()
        self.assertTrue(apartment_alpha.is_avaliable,
                        'Apartamento deve estar disponível ao ser cadastrado.')

        response_alpha = self.client.post('/rent/apartments/', {
            'name': 'AP02',
            'start_price': 40
        })
        self.assertEqual(response_alpha.status_code, 200,
                         'Apartamento não foi criado com sucesso.')

        form_bravo = AddApartmentForm({
            'name': 'AP02'
        })
        self.assertFalse(form_bravo.is_valid())
        self.assertHasErrors(form_bravo, 'start_price')

        form_unique = AddApartmentForm({
            'name': 'AP03',
            'start_price': 30
        })
        form_unique.save()

        form_not_unique = AddApartmentForm({
            'name': 'AP03',
            'start_price': 676.40
        })

        self.assertHasErrors(form_not_unique, 'name')

        apartment_bravo = self.seed(Apartment)
        response_bravo = self.client.get('/rent/apartments/')
        self.assertEqual(response_bravo.status_code, 200)
        self.assertContains(response_bravo, apartment_bravo.name,
                            msg_prefix='Apartamento adicionado deve aparecer na lista')
        self.assertContains(response_bravo, apartment_bravo.current_price(),
                            msg_prefix='Preço do apartamento deve aparecer na lista')
