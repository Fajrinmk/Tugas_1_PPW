from django.shortcuts import render



response = {'author': "Hepzibah Smith"}
birthday = '01 Jan'
gender = 'Female'
expertise = ['Marketing','Collector','Public Speaking']
description = 'Antique expert. Experience as marketer for 10 years'
email = 'hello@smith.com'

def index(request):
    html = 'halaman_profile/halaman_profile.html'
    response['birthday'] = birthday
    response['gender'] = gender
    # response['expertise'] = expertise  
    response['description'] = description
    response['email'] = email  
    return render(request, 'halaman_profile.html', response)