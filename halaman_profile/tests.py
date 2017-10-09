from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index
from .views import index, username,birthday,gender,expertise,description,email
# Create your tests here.

class halaman_profile(TestCase):

    def test_halaman_profile_url_is_exist(self):
        response = Client().get('/halaman_profile/')
        self.assertEqual(response.status_code, 200)
    
    def test_halaman_profile_using_index_func(self):
        found = resolve('/halaman_profile/')
        self.assertEqual(found.func, index)

    def test_halaman_profile_dict(self):
        # Check whether bio_dict is not None Object
        self.assertIsNotNone(username)
        self.assertIsNotNone(birthday)
        self.assertIsNotNone(gender)
        self.assertIsNotNone(expertise)
        self.assertIsNotNone(description)
        self.assertIsNotNone(email)

        # Check whether description entry is less than 3 
        self.assertTrue(len(description) >= 5)

        #Check whether expertise is less than 3
        self.assertTrue(len(expertise) >= 3)



