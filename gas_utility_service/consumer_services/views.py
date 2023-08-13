from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout

# Create your views here.
from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import User_info

def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username = request.POST['username'])
                return render (request,'signup.html', {'error':'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'],email=request.POST['email'])
                auth.login(request,user)
                return redirect('/profile', request)
        else:
            return render (request,'signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('/profile', request)
        else:
            return render (request,'login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('home')

def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

def profile(request):
    return render(request, 'profile.html')

def submit_request(request):
    try:
        user = request.user
    except:
        return render(request,'error.html')
   #handle case when user with that id does not exist
    if request.method == 'POST':
        try:
            file = request.FILES["file"]
        except:
            file = None
        User_info.objects.create(user=user, issue= request.POST['Issue'], address = request.POST['address'], 
                                 extra_info = request.POST['extra_info'], file=file)
        return render(request,'success.html')
    else:
        return render(request,'profile.html')
    
def show_complaints(request):
    try:
        user = request.user
    except:
        return render(request,'error.html')
    mydata = User_info.objects.filter(user=user).values()
    template = loader.get_template('profile_complaints.html')
    context = {
        'mymembers': mydata,
    }
    return HttpResponse(template.render(context, request))
