from django.conf.urls import url
from .views import index, tambah_teman,delete


urlpatterns=[
	url(r'^$', index, name='index'),
	url(r'^tambah_teman', tambah_teman, name='tambah_teman'),
	url(r'^delete/(?P<id>\d+)/$',delete, name='delete'),
]