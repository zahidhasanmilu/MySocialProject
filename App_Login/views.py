from django.shortcuts import render, HttpResponseRedirect, HttpResponse, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .forms import CreateNewUserForm
from .models import UserProfile


# Create your views here.
def home(request):
    return render(request, 'App_Login/home.html')


def signup(request):
    if request.method == 'POST':
        form = CreateNewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_profile = UserProfile(user=user)
            user_profile.save()
            # return HttpResponseRedirect(reverse('signin'))
            return HttpResponse('Signup succesfully')
    else:
        form = CreateNewUserForm()

    context = {
        'form': form
    }
    return render(request, 'App_Login/signup.html', context)


def signin(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'App_Login/signin.html', context)


def signout(request):
    logout(request)
    return HttpResponse('Signout succesfully')
