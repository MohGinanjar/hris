from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.http import HttpResponse
from django.template import loader

@unauthenticated_user
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("hris:home")
            else:    
                msg = 'Invalid credentials \n Please try again ...'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

@login_required(login_url="hris:login")
def index(request):
    return render(request, "index.html")

@login_required(login_url="hris:login")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:
        
        load_template = request.path.split('/')[-1]
        html_template = loader.get_template( load_template )
        return HttpResponse(html_template.render(context, request))
        
  

        html_template = loader.get_template( 'error-404.html' )
        return HttpResponse(html_template.render(context, request))

    except:
    
        html_template = loader.get_template( 'error-500.html' )
        return HttpResponse(html_template.render(context, request))
        
# Create your views here.



@login_required(login_url="hris:login")
def LogoutView(request):
    logout(request)
    return redirect('hris:login')
    
@login_required(login_url="hris:login")
def error404(request):
    return render(request, 'error-404.html')


@login_required(login_url="hris:login")
@allowed_users(allowed_roles=['Administrator'])
def home(request):
    context = {}
    return render(request, 'home.html', context)