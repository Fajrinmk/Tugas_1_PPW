from django.conf.urls import url
from .views import index, tambah_teman


urlpatterns=[
url(r'^$', index, name='index'),
]