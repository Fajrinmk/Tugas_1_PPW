from django.test import TestCase
from .views import index, tambah_teman

# Create your tests here.
 #mengambil elemen pada url add_friend
def test_add_friend_url_is_exist(self):
	response = Client().get('/add_friend/')
	self.assertEqual(response.status_code,200)

#memastikan bahwa template yang digunakan adalah add_friend.html
def test_add_friend_url_using_html(self):
	response = Client().get('/add_friend/')
	self.assertTemplateUsed(response,'add_friend.html')

 #memeriksa apakah pada views.py terdapat method index
def test_add_friend_url_using_index(self):
	found = resolve('/add_friend/')
	self.assertEqual(found.func,index)
