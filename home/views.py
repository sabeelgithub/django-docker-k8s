from django.shortcuts import render
from django.http import HttpResponse
from .models import Category
from rest_framework.response import Response

# Create your views here.
def Welcome(request):
    return HttpResponse("Welcome to sample Django application")
