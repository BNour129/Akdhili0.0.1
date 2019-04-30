from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from . import forms


# Create your views here.
# 4 types taa kadia li homa fast food, aliments nutritifs, service social w kadhia personnalisée 
