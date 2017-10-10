from django.shortcuts import render
from .models import DataProfil, Expertise

profil = DataProfil.objects.get(username='Hepzibah Smith')

def index(request):
    response['username'] =profil.nama
    response['birthday'] = profil.birthday
    response['gender'] = profil.gender
    response['expertise'] = profil.expertise
    response['description'] = profil.description
    response['email'] = profil.email

    html = 'halaman_profile/halaman_profile.html'

    return render(request,html,response)
