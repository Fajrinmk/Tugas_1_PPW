from django.test import TestCase
from django.test import Client
from django.urls import resolve
from datetime import datetime, date
from .views import index, profile_name,birthdate,gender,email,desc_profile,expert
import unittest
from .models import DataProfile

# Create your tests here.
class HalamanProfileUnitTest(TestCase):
    def setUp(self):
        Profile = DataProfile(name= profile_name, birthday = birthdate, gender = gender,expertise = expert, email = email, description = desc_profile, id = 1 )
        Profile.save()     
    
    def test_name_is_exist(self):
        response = Client().get('/halaman_profile/')
        self.assertEqual(response.status_code,200)

    def test_using_index_func(self):
        found = resolve('/halaman_profile/')
        self.assertEqual(found.func, index)

    def test_all_profile_is_exist(self):
        #to check whether name is not none
        self.assertIsNotNone(profile_name)
        self.assertIsNotNone(birthdate)
        self.assertIsNotNone(gender)
        self.assertIsNotNone(email)

    def test_description_is_written(self):
        #check whether there is any description
        self.assertIsNotNone(desc_profile)

        #the description is filled with 20 characters at least
        self.assertTrue(len(desc_profile) >= 20)

    def test_expertise_is_more_than_3(self):
        self.assertTrue(len(expert) >= 3)

    # def test_model_profile(self):
    #     profile_name = 'gaga'
    #     birthday = date(1997,7,15)
    #     gender = 'female'
    #     expert = 'run,climb,write'
    #     email = 'gaga@gmail.com'
    #     description = 'ahahahahahahah'
    #     response = Client().post('/halaman_profile/handle_edit_profile/', {'name': profile_name, 'birthday' : birthday, 'gender' : gender, 'expertise' : expert, 'email' : email, 'description' : description})
    #     self.assertEqual(response.status_code,200)
    #     response =Client.get('/halaman_profile/')
    #     html_response = response.content.decode('utf8')
    #     self.assertIn(name,html_response)
    #     self.assertIn(birthday,html_response)
    #     self.assertIn(gender,html_response)
    #     self.assertIn(expert,html_response)
    #     self.assertIn(email,html_response)
    #     self.assertIn(description,html_response)

    # def test_edit_profile_redirect(self):
    #     response = Client().post('/halaman_profile/show_form_edit_profile/')
    #     self.assertEqual(response.status_code,200)

    

    
