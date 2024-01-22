from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.saleshome,name="saleshome"),
    path('add', views.adddata, name="adddata"),
    path('insert', views.insert),
]