from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
# Create your views here.


def login(request):
	if request.method=='POST':
		userid = request.POST['userid']
		password = request.POST['password']
		user = authenticate(username=userid,password=password)
		if user is not None:
			return redirect('home')
		else :
			return redirect('login')
	return render(request,'users/login.html')


def home(request):
	return HttpResponse(request,'gsk')