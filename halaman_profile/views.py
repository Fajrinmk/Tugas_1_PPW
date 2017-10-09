from django.shortcuts import render
from django.http import HttpResponseRedirect

username = 'Hepzibah Smith'
# landing_page_content = 'profile page'
birthday = '01 Jan'
gender = 'Female'
expertise = 'Marketing Collector Public Speaking'
description = 'Antique expert. Experience as marketer for 10 years'
email = 'hello@smith.com'

def index(request):
    html = 'halaman_profile/halaman_profile.html'
    response = {'username' : username, 'bithday' : birthday, 'gender' : gender, 'expertise' : expertise, 'description':description, 'email': email}  
    return render(request, halaman_profile.html, response)