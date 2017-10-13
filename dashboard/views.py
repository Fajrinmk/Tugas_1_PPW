from django.shortcuts import render
from django.http import HttpResponseRedirect
from update_status.models import Status
from halaman_profile.views import profile_name
from add_friend.models import new_friend

def index(request):
    response = {}
    response['profile_name'] = profile_name
    stat = Status.objects.all().order_by('-id')
    if len(stat) == 0:
    	response['database'] = "Belum ada status"
    else:
    	response['database'] = stat[0]    
    response['feed'] = len(stat)
    listFriend = new_friend.objects.all()
    response['numberOfFriends'] = len(listFriend)
    return render(request, 'dashboard/dashboard.html', response)
