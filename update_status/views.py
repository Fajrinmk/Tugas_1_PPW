from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import Status_Form
from .models import Status

response = {}
def index(request):    
    status = Status.objects.all()
    response['status'] = status
    html = 'status/status.html'
    response['Status_form'] = Status_Form
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
