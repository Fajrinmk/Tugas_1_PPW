from django.shortcuts import render
from django.http import HttpResponseRedirect

response = {'author': "Hepzibah Smith"}
landing_page_content = 'profile page'
birthday = '01 Jan'
gender = 'Female'
expertise = 'Marketing Collector Public Speaking'
description = 'Antique expert. Experience as marketer for 10 years'
email = 'hello@smith.com'

def index(request):
    html = 'halaman_profile/halaman_profile.html'
    response['content'] = landing_page_content
    response['birthday'] = birthday
    response['gender'] = gender
    response['expertise'] = expertise  
    response['description'] = description
    response['email'] = email  
    return render(request, html, response)