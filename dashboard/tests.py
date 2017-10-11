from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index

class DashboardUnitTest(TestCase):
    def test_dashboard_url_is_exist(self):
        response = Client().get('/dashboard/')
        self.assertEqual(response.status_code,200)

    def test_using_index_func(self):
        found = resolve('/dashboard/')
        self.assertEqual(found.func, index)