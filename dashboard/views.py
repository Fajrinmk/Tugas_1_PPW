from django.shortcuts import render

def index(request):
    response = {'name': "Fajrin", 'age': "17"}
    return render(request, 'dashboard.html', response)
