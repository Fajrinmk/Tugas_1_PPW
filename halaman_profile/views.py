from django.shortcuts import render
from .models import DataProfil, Expertise

profil = DataProfil.objects.get(nama='Hepzibah Smith', birthday = '01 jan', gender = 'Female', expertise = 'Marketing, Collector, Public Speaking', description = 'Antique expert. Experience as marketer for 10 years', email = 'hello@smith.com')

def index(request):
    response['nama'] =profil.nama
    response['birthday'] = profil.birthday
    response['gender'] = profil.gender
    response['expertise'] = profil.expertise
    response['description'] = profil.description
    response['email'] = profil.email

    html = 'profil.html'

    return render(request,html,response)
