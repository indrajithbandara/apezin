from app.base.tests import BaseTestCase
from app.rent.models import Apartment, Price


class ApartmentTestCase(BaseTestCase):
    """
    TestCase to Apartment Model
    """

    def test_add(self):
        """
        Try to app an apartment
        """
        apartment = self.seed(model=Apartment)

        self.assertTrue(apartment.is_avaliable,
                        'Apartment must be avaliable at creation')

        response = self.client.get('/rent/apartments/')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, apartment.name,
                            msg_prefix='Inserted apartment not appearing in list')
