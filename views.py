from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import DataProfil

# username = 'Hepzibah Smith'
# birthday = '01 Jan'
# gender = 'Female'
# expertise = 'Marketing Collector Public Speaking'
# description = 'Antique expert. Experience as marketer for 10 years'
# email = 'hello@smith.com'

profil = DataProfil.objects.create(username ='Hepzibah Smith', birthday ='01 jan',gender = 'Female', expertise = 'Marketing Collector Public Speaking',description = 'Antique expert. Experience as marketer for 10 years', email ='hello@smith.com' )
profil.save()

def index(request):
    html = 'halaman_profile/halaman_profile.html'
    response['username']= username
    response ['birthday'] = birthday
    response ['gender'] = gender
    response ['expertise'] = expertise
    response ['description'] = description
    response ['email'] = email
    return render(request, 'halaman_profile/halaman_profile.html', response)