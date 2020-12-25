from django.shortcuts import render, redirect
from django.http import HttpResponse
from homepage.forms import Registrationform
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def userlogin(request):
    loginform = UserCreationForm()
    return render(request, 'login.html', {'loginform': loginform})

def register(request):
    if request.method=='POST':
        registration_from = Registrationform(request.POST)
        if registration_from.is_valid():
            registration_from.save()
            return redirect('login')
    else:
        registration_from = Registrationform()
    return render(request, 'register.html', {'registration_form': registration_from})    


    return render(request, 'login.html')

def about(request):
    return render(request, 'about.html')


def profile(request):
    return render(request, 'profile.html')



