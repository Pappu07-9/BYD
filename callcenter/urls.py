from django.urls import path
from . import views

urlpatterns = [
    path('', views.callhome, name="callcenterhome"),
    path('regularcall', views.startcall),
]