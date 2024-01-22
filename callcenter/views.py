from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.messages import constants as messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import get_user_model

User = get_user_model()
# Create your views here.

