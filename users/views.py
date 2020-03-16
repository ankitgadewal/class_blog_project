from django.shortcuts import render, HttpResponse
from .models import Register

# Create your views here.
def index(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        newuser = Register(name=name, email=email, password=password)
        newuser.save()
    return render(request, 'index.html')
