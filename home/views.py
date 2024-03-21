from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Welcome(request):
    return HttpResponse("Welcome to sample Django application")