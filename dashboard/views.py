from django.shortcuts import render
from django.http import HttpResponseRedirect
from update_status.models import Status
from halaman_profile.views import profile_name
from add_friend.models import new_friend
from datetime import *

def index(request):
    response = {}
    response['profile_name'] = profile_name
    stat = Status.objects.all().order_by('-id')
    if (len(stat) > 0):
    	message = stat[0]
    	newMessage = message.status
    	time = message.created_date
    else:
    	newMessage = "You have not posted yet" 
    	time = date(datetime.now().year,datetime.now().month,datetime.now().day)
    response['latestMessage'] = newMessage
    response['latestTime'] = time 
    response['feed'] = len(stat)
    listFriend = new_friend.objects.all()
    response['numberOfFriends'] = len(listFriend)
    return render(request, 'dashboard/dashboard.html', response)
