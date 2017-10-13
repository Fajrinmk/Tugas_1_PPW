from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Status_Form
from .models import Status
from halaman_profile.views import profile_name
from halaman_profile.models import DataProfile
##ini buat ngambil username dari halaman profile

response = {}
def index(request):
    user = DataProfile.objects.first()
    response['author'] = 'Patricia Christiana'
    response['profile_name'] = user.name    
    html = 'update_status/status.html'
    response['Status_form'] = Status_Form
    response['status'] = Status.objects.all().order_by('-id')
    return render(request, html, response)

def add_status(request):
    form = Status_Form(request.POST or None)
    if(request.method == 'POST' and form.is_valid()):
        response['status'] = request.POST['status']
        status = Status(status=response['status'])
        status.save()
        return HttpResponseRedirect('/update-status/')
        
    else:
        return HttpResponseRedirect('/update-status/')
