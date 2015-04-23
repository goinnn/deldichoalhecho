from django.test import TestCase
from promises_instances.models import DDAHCategory, DDAHInstance
from instances.models import Instance
from popolo.models import Person
from promises.models import Promise


class DDAHInstancesTestCase(TestCase):
    def setUp(self):
        self.person = Person.objects.create(name=u"A person")

    def test_create_instance(self):
        '''Create an instance'''
        ddah_instance = DDAHInstance.objects.create(label='label', title='the title')
        self.assertTrue(ddah_instance)
        self.assertIsInstance(ddah_instance, Instance)

    def test_an_instance_can_have_categories(self):
        ddah_instance = DDAHInstance.objects.create(label='label', title='the title')
        category = DDAHCategory.objects.create(name="Education", instance=ddah_instance)

        self.assertIn(category, ddah_instance.categories.all())