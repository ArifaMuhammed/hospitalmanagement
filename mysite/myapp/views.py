from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Doctors
from .models import Department, Booking,Career
from .import forms
from .forms import BookingForm,careerform,contactform
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages


# Create your views here.
def mainhome(request):
    return render(request, "Home.html")

def index(request):
    person = {
        'name': 'arifa',
        'age': 25
    }
     # return HttpResponse("Home Page")
    return render(request, "homepage.html", person)
def base(request):
    return render(request, "base.html")
def about(request):
    num = {
        'num1': 20
    }
    return render(request, "about.html", num)

def doct(request):
    dict_docs = {
        'doctors': Doctors.objects.all()

    }
    return render(request, "doctors.html", dict_docs)

def contact(request):
    return render(request, "contact.html")
def depart(request):
    dict_dept = {
          'dept': Department.objects.all()
          }
    return render(request, "department.html", dict_dept)

def career_view(request):
    form=careerform
    mydict={
        "form":form,
        # 'jobkey': Job.objects.all()
    }
    return render(request,"career.html",mydict)
def contact(request):
    form=contactform
    mydict={
        "form":form
    }
    return render(request, "contact.html" ,mydict)
def booking(request):

    # if request.method == "POST":
    #     form = BookingForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return render(request, 'c.html')
    form = BookingForm
    mydict = {
        "form": form
    }
    return render(request, "booking.html", context=mydict)


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pswrd')
        cpass = request.POST.get('cnfrmpswrd')
        if password == cpass:
            if User.objects.filter(username=username).exists():
                messages.add_message(request, messages.ERROR, 'Username already exists')
                return HttpResponseRedirect(reverse('signup'))
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.set_password(password)
                user.save()
                return HttpResponseRedirect(reverse('login'))
        else:
            messages.add_message(request, messages.ERROR, 'password not matching')
            return HttpResponseRedirect(reverse('signup'))
    else:
        return render(request, "reg.html")

def login_user(request):
    if request.method == 'POST':
        print("hi")
        username = request.POST['username']
        password = request.POST['pswrd']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return  HttpResponseRedirect(reverse('base'))
        else:
            messages.add_message(request, messages.ERROR, 'Invalid username or password')
            return HttpResponseRedirect(reverse('login'))
    else:
        return render(request, "login.html")


# #
# #
# def logout(request):
#     auth.logout(request)
#     return redirect('home')
