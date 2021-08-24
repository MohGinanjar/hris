from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.decorators import login_required


def logbook(request):
    return render(request, 'logbook.html')

def profile(request):
    return render(request, 'profile.html')

def icon(request):
    return render(request, 'icons.html')

def calender(request):
    return render(request, 'calendar.html')