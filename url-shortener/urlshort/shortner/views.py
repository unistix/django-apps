from django.shortcuts import render, redirect
import uuid 
from .models import Url
from django.http import HttpResponse

# Create your views here.

def index(request):
	return render(request, 'index.html')

def create(request):
	if request.method == 'POST':
		url = request.POST['link'] #getting what user put as link and storing it in Var named URL
		uid = str(uuid.uuid4())[:5] #assign a particular ID to that variable the ID can be used to generate a shortened link

		#after we get this data we need to save ther data in our database
		new_url = Url(link=url,uuid=uid) #this creates a new URL in the DB
		new_url.save()
	return HttpResponse(uid)

def go(request, pk):
	#get pk which is a dynamic url creates a /string and saves it in a variable named pk
	#when a user goes to the new url, the dynamic string will be replaced with the uuid
	#then we search through the model and make sure the uuid is present in our model and a link has been assigned to it.
	#the we get the link using url_details.link and return the redirect action which redirects the user to that link 
	url_details = Url.objects.get(uuid=pk)
	# return redirect(url_details.link) leads to page not found error needs to be passed as url

	#"https://"+ - removed as redirected kept taking out colon
	return redirect(url_details.link)

	
