from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def open_page (request):
    if request.method == 'POST':
        return render(request, 'accountapp/open_page.html',
                      context={'text': ' POST METHOD!'})
    else:
        return render(request, 'accountapp/open_page.html',
                      context={'text': ' GET METHOD!'})