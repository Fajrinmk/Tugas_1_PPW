from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index
# Create your tests here.

class halaman_profile(TestCase):

    def test_halaman_profile_url_is_exist(self):
        response = Client().get('/halaman_profile/')
        self.assertEqual(response.status_code, 200)
    
    def test_halaman_profile_using_index_func(self):
        found = resolve('/halaman_profile/')
        self.assertEqual(found.func, index)

