from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, tambah_teman
from .models import new_friend


# Create your tests here.
 #mengambil elemen pada url add_friend
class UpdateUnitTest(TestCase):
    def test_add_friend_url_is_exist(self):
        response = Client().get('/add_friend/')
        self.assertEqual(response.status_code,200)

 #memeriksa apakah pada views.py terdapat method index
    def test_add_friend_url_using_index(self):
        found = resolve('/add_friend/')
        self.assertEqual(found.func,index)

    def test_model_can_create_new_status(self):
        temanku = new_friend.objects.create(name='test',heroku_link='http://www.color-hex.com/')
        counting_all_available_friend = new_friend.objects.all().count()
        self.assertEqual(counting_all_available_friend, 1)

    def test_model_post_success_and_render_the_result(self):
        test = 'Anonymous'
        response_post = Client().post('/add_friend/tambah_teman', {'name':test, 'heroku_link': 'http://www.color-hex.com/'})
        self.assertEqual(response_post.status_code, 302)

        response= Client().get('/add_friend/')
        html_response = response.content.decode('utf8')
        self.assertIn(test, html_response)

    def test_model_post_failed_and_render_the_result(self):
        test = 'http://www.color-hex.com/'
        response_post = Client().get('/add_friend/tambah_teman', {'name':test, 'heroku_link': 'a'})
        self.assertEqual(response_post.status_code, 302)

        response= Client().get('/add_friend/')
        html_response = response.content.decode('utf8')
        self.assertNotIn(test, html_response)

    def test_model_post_error_and_render_the_result(self):
        test = 'Anonymous'
        response_post = Client().post('/add_friend/tambah_teman', {'name': test, 'heroku_link': 'a'})
        self.assertEqual(response_post.status_code, 302)

        response= Client().get('/add_friend/')
        html_response = response.content.decode('utf8')
        self.assertNotIn(test, html_response)

    def test_delete_feature(self):
        #digunakan untuk mengecek apakah linknya dari add_todo aktif
        test = "ini adalah test saja"
        response_post = Client().post('/add_friend/tambah_teman', {'name': test, 'heroku_link': 'http://www.color-hex.com/'}) #post(link metodrnya, isi bi=uat si metod)
        self.assertEqual(response_post.status_code,302)

        response = Client().get('/add_friend/')
        html_response = response.content.decode('utf8')
        self.assertIn(test, html_response)     
        

        response = Client().post('/add_friend/delete/1/')
        self.assertEqual(response.status_code,302)

        response = Client().get('/add_friend/')
        html_response = response.content.decode('utf8')
        self.assertNotIn(test, html_response)