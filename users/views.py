from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect
from .models import Register
import time
from django.contrib import messages



# Create your views here.
def register(request):
    url = request.get_host()
    return render(request, 'register.html', {'url':url})

def login(request):
    url = request.get_host()
    return render(request, 'login.html', {'url':url})

def reg(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        newuser = Register(name=name, email=email, password=password)
        newuser.save()
        messages.success(request, 'registration successful you can login now...')
        return redirect(to='/login')

def checklogin(request):
    if request.is_secure():
        return HttpResponse("connection is secure ")
    else:
        if request.method == 'POST':
            email = request.POST['email']
            password = request.POST['password']
            user = Register.objects.filter(email=email, password=password).values()
            
            if user:
                print(user)
                username = user[0]['name']
                print(username)
                time.sleep(1.5)
                messages.success(request, 'login successful')
                return render(request, 'myprofile.html', {'username':username})
            else:
                messages.warning(request, 'Invalid Credentials')
                return redirect(to="/login")

def index(request):
    return render(request, 'index.html')