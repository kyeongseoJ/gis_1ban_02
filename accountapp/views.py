from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def open_page (request):
    return render(request, 'accountapp/open_page.html')