from django import views
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.allemp, name='allemp'),
    path('viewall', views.view, name='view'),
    path('addemp', views.addemp, name='addemp'),
]
