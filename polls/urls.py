from django import views
from django.contrib import admin
from django.urls import path
from . import views

app_name="polls"

urlpatterns = [
    path('', views.allemp, name='allemp'),
    path('viewall', views.view, name='view'),
    path('addemp', views.addemp, name='addemp'),
    path('deleteemp/<id>', views.Deleteemp, name='Deleteemp'),
    path('updateemp/<id>',views.Updateemp, name='Updateemp'),
]
