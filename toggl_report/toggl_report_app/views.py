from django.shortcuts import render
from django.http import HttpResponce

def index(request):
    return HttpResponce("Hello, world. You're at the toggl_report_app index.")

# Create your views here.
