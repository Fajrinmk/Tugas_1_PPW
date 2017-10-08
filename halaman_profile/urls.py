from django.conf.urls import url
from .views import index, message_post, message_table

urlpatterns = [
    url(r'^$', index, name='index'),

 ]