from django.shortcuts import render
from datetime import datetime, date
from .models import DataProfile

# Create your views here.
profile_name = 'Gigi Hadid' #TODO implement your name here
birth_date = date(1995,4,23) #TODO implement your birthday
birthdate = birth_date.strftime('%d %B %Y')
gender = 'Female' #TODO implement your gender
email = 'gigihadid@gmail.com' #TODO implement your email
desc_profile = "victoria's secret model lalala lilili yeyeye"
#TODO implement your expertise minimal 3
expert = ["fashion model", "actress", "wawww"]

response = {}
def index(request):
    # response['author'] = "Patricia Christiana"
    # response['Name'] = profile_name
    # response['Birthday'] = birthdate
    # response['Gender'] = gender
    # response['expertise'] = expert
    # response['Email'] = email
    # response['Description'] = desc_profile

    Profile = DataProfile(name= profile_name, birthday = birthdate, gender = gender,expertise = expert, email = email, description = desc_profile )
    response = {'Name':Profile.name, 'Birthday':Profile.birthday,'Gender':Profile.gender,'Expertise':Profile.expertise,'Email':Profile.email,'Description':Profile.description}
    return render(request, 'halaman_profile.html', response)
    
