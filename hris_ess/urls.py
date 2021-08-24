from django.urls import path, re_path
from . import views
from . import auth

urlpatterns = [
	path('', auth.login_view, name="login"),
	path('logout/', auth.LogoutView, name="logout"),
	path('error404/', auth.error404, name="error404"),
	path('home/', auth.home, name="home"),
	path('logbook/', views.logbook, name="logbook"),
	path('icon/', views.icon, name="icon"),
	path('profile/', views.profile, name="profile"),
	path('calender/', views.calender, name="calender"),
]