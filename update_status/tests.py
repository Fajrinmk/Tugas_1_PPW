from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index,add_status
from .models import Status
from .forms import Status_Form
from halaman_profile.models import DataProfile
from halaman_profile.views import profile_name, birthdate, gender, expert, email, desc_profile

class UpdateStatusUnitTest(TestCase):
	def setUp(self):
		Profile = DataProfile(name= profile_name, birthday = birthdate, gender = gender,expertise = expert, email = email, description = desc_profile, id = 1 )
		Profile.save()

	def test_updateStatus_url_is_exist(self):
		response = Client().get('/update-status/')
		self.assertEqual(response.status_code, 200)

	def test_updateStatus_using_index_func(self):
		found = resolve('/update-status/')
		self.assertEqual(found.func, index)

	def test_model_can_create_new_status(self):
		# Creating a new activity
		new_status = Status.objects.create(status='mengerjakan tugas 1 ppw')
		# Retrieving all available activity
		counting_all_available_status = Status.objects.all().count()
		self.assertEqual(counting_all_available_status, 1)

	def test_updateStatus_post_success_and_render_the_result(self):
		new_status = Status.objects.create(status='mengerjakan tugas 1 ppw')
		response_post = Client().post('/update-status/add_status', {'status': new_status})
		self.assertEqual(response_post.status_code, 301)

		response= Client().get('/update-status/')
		html_response = response.content.decode('utf8')
		self.assertIn('mengerjakan tugas 1 ppw', html_response)

	def test_updateStatus_post_error_and_render_the_result(self):
		test = 'Anonymous'
		response_post = Client().post('/update-status/add_status', {'status': ''})
		self.assertEqual(response_post.status_code, 301)
		response= Client().get('/update-status/')
		html_response = response.content.decode('utf8')
		self.assertNotIn(test, html_response)

	def test_form_todo_input_has_placeholder_and_css_classes(self):
		form = Status_Form()
		self.assertIn('class="status-form-input', form.as_p())
		self.assertIn('id="id_status"', form.as_p())
	

	def test_form_validation_for_blank_items(self):
		form = Status_Form(data={'status': ''})
		self.assertFalse(form.is_valid())
		self.assertEqual(
		    form.errors['status'],
		    ["This field is required."]
		    )

	def test_update_status_post_fail(self):
		response = Client().post('/update-status/add_status', {'message': ''})
		self.assertEqual(response.status_code, 301)