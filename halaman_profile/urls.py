from django.conf.urls import url
from .views import index, handle_edit_profile,show_form_edit_profile

#url for app
urlpatterns = [
    url(r'^handle_edit_profile',handle_edit_profile,name='handle_edit_profile'),
    url(r'^show_form_edit_profile',show_form_edit_profile,name='show_form_edit_profile'),
    url(r'^$', index, name='index'),
]
