from app.base.tests import BaseTestCase
from app.rent.models import Apartment, Price
from pprint import pprint


class ApartmentTestCase(BaseTestCase):
    """
    TestCase to Apartment Model
    """

    def test_add(self):
        """
        Try to app an apartment
        """
        apartment = self.seed(model=Apartment, data={
            'name': 'AP02'
        })

        prices = self.seed(model=Price, times=3, data={

        })

        self.assertTrue(apartment.is_avaliable,
                        'Apartment must be avaliable at creation')

        response = self.client.get('/rent/apartments/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, apartment.name,
                            'Inserted apartment not appearing in list')
