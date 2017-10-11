from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, profile_name,birthdate,gender,email,desc_profile,expert
import unittest

# Create your tests here.
class HalamanProfileUnitTest(TestCase):
    def test_name_is_exist(self):
        response = Client().get('/halaman-profile/')
        self.assertEqual(response.status_code,200)

    def test_using_index_func(self):
        found = resolve('/halaman-profile/')
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

    

    
