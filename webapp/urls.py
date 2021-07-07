"""cpanel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.urls import path
from . import views, forms
from django.contrib.auth.views import LoginView

urlpatterns = [
    url(r'^login', views.singIn),
    url(r'^postsign/', views.postsign),
    url(r'^logout/', views.logout, name="log"),
    url(r'^signup/', views.signUp, name='signup'),
    url(r'^postsignup/', views.postsignup, name='postsignup'),
    url(r'^guia/', views.mostrarguia, name='guia'),
    url(r'^create/', views.create, name='create'),
    url(r'^post_create/', views.post_create, name='post_create'),
    url(r'^check/', views.check, name='check'),
    url(r'^modificar/', views.modificar, name='modificar'),
    url(r'^eliminar/', views.eliminar, name='eliminar'),

    path('', views.home, name='home'),
    path('iniciarsesion/',  LoginView.as_view(template_name='new/login.html',  authentication_form=forms.LoginForm), name="iniciarsesion"),
    path('app/', views.app, name='app'),
    path('autodiagnostico/', views.autodiagnostico, name='autodiagnostico'),
    path('autodiagnostico/formulario/', views.formulario, name='formulario'),
    path('autodiagnostico/resultados/', views.resultados, name='resultados'),
    path('autodiagnostico/pasados/<int:id>/', views.pasados, name='pasados'),
]
