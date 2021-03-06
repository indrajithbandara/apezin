from django.test import TestCase, Client
from django_seed import Seed

required_field_validator = 'Este campo é obrigatório.'


class BaseTestCase(TestCase):
    client = Client()

    def seed(self, model, times=1, data=None):
        """
        Generate data in refered but doenst store it in database

        :model: Model name to seed\n
        :times: How many objects to add\n
        :data: Override default faker generated data

        return inserted objects
        """
        # create seeder

        seeder = Seed.seeder()

        # add model objects

        if data:
            seeder.add_entity(model, times, data)
        else:
            seeder.add_entity(model, times)

        # get inserted object

        inserted_objects = seeder.execute()
        id_list = inserted_objects[model]

        # return a QuerySet with inserted objects
        # by filtering id

        if len(id_list) > 1:  # Return a list of inserted objects
            return model.objects.filter(id__in=id_list)
        else:  # Return only one inserted object
            return model.objects.get(id=id_list[0])

    def assertHasErrors(self,  form, field_name):
        """
        Check if :field_name: has an error inside :form:
        """
        return field_name in form.errors
