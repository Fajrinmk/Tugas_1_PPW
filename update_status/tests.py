from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index,add_status
from .models import Status
from .forms import Status_Form

class UpdateStatusUnitTest(TestCase):
	def test_updateStatus_url_is_exist(self):
		response = Client().get('/update-status/')
		self.assertEqual(response.status_code, 200)

	def test_updateStatus_using_index_func(self):
		found = resolve('/update-status/')
		self.assertEqual(found.func, index)

	def test_model_can_create_new_status(self):
		# Creating a new activity
		new_activity = Status.objects.create(status='mengerjakan tugas 1 ppw')
		# Retrieving all available activity
		counting_all_available_status = Status.objects.all().count()
		self.assertEqual(counting_all_available_status, 1)

	def test_updateStatus_post_success_and_render_the_result(self):
		test = 'Anonymous'
		response_post = Client().post('/update-status/add_status', {'status': test})
		self.assertEqual(response_post.status_code, 302)

		response= Client().get('/update-status/')
		html_response = response.content.decode('utf8')
		self.assertIn(test, html_response)

	def test_updateStatus_post_error_and_render_the_result(self):
		test = 'Anonymous'
		response_post = Client().post('/update-statu/add_status', {'status': ''})
		self.assertEqual(response_post.status_code, 302)
		response= Client().get('/update-status/')
		html_response = response.content.decode('utf8')
		self.assertNotIn(test, html_response)
