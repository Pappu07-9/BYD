from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.saleshome),
    path('add', views.adddata),
    path('insert', views.insert),
]