from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def open_page (request):
    return HttpResponse('Open the World!')