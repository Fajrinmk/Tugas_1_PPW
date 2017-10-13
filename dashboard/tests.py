from django.test import TestCase
from django.test import Client
from django.urls import resolve
from update_status.models import Status
from .views import index

class DashboardUnitTest(TestCase):
    def test_dashboard_url_is_exist(self):
        response = Client().get('/dashboard/')
        self.assertEqual(response.status_code,200)

    def test_using_index_func(self):
        found = resolve('/dashboard/')
        self.assertEqual(found.func, index)

    def test_if_user_havent_posted(self):
        message = "You have not posted yet"
        response = Client().get('/dashboard/')
        html_response = response.content.decode('utf8')
        self.assertIn(message, html_response)

    def test_if_user_have_posted(self):
        message = "You have not posted yet"
        tryStatus = Status.objects.create(status='woyyy hehehe')
        response = Client().get('/dashboard/')
        html_response = response.content.decode('utf8')
        self.assertNotIn(message,html_response)
