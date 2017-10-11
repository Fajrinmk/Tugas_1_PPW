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

def test_delete_feature(self):
        #digunakan untuk mengecek apakah linknya dari add_todo aktif
    test = "ini adalah test saja"
    response_post = Client().post('/add_friend/tambah_teman', {'name': test, 'heroku_link': 'www.google.com'}) #post(link metodrnya, isi bi=uat si metod)
    self.assertEqual(response_post.status_code,302)

    response = Client().get('/add_friend/')
    html_response = response.content.decode('utf8')
    self.assertIn(test, html_response)     
        

    response = Client().post('/add_friend/delete/1/')
    self.assertEqual(response.status_code,302)

    response = Client().get('/add_friend/')
    html_response = response.content.decode('utf8')
    self.assertNotIn(test, html_response)