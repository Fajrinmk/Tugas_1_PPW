from django.shortcuts import render
from .models import new_friend

# Create your views here.
response = {}
def index(request):
	#inisiasi elemen apa saja yang akan dimasukan dalam add_friend.html
	response['author'] = 'Josua Christanto'
	friends = new_friend.objects.all()
	response['new_friend'] = friends
	html = 'add_friend/add_friend.html'
	return render(request,html,response) #mengirimkkan semua elemen dalam response ke alamat html

def tambah_teman(request):
	if(request.method=='POST'):
		response['name'] = request.POST['name']
		response['heroku_link'] = request.POST['heroku_link']
		friends = new_friend(name=response['name'],heroku_link=response['heroku_link'])
		friends.save()
		response[new_friend] = friends
		return HttpResponseRedirect('/add_friend/')
	else:
		return HttpResponseRedirect('/add_friend/')
