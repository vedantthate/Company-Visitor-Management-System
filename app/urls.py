"""
URL configuration for Company_visiter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.Login,name='login'),
    path('register',views.Register,name='register'),
    path('forgetpassword',views.Forgetpass,name='forgetpassword'),
    path('dashboard',views.Dashboard,name='dashboard'),
    path('newvisiter',views.Newvisiter,name='newvisiter'),
    path('managevisiter',views.Managevisiter,name='managevisiter'),
    path('visitbydate',views.Visitbydate,name="visitbydate"),
    path("visiablebydate",views.Visiablebydate, name="visiablebydate"),
    path('updatevisiter/<int:id>',views.Update_visiter,name="updatevisiter"),
    path('logout',views.Logout,name='logout'),
    path('profile',views.Profile_admin,name='profile'),
    path('newpassword',views.Newpassword,name='newpassword')
]
