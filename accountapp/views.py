from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import Open_Page


def open_page (request):
    if request.method == 'POST':

        temp = request.POST.get('open_page_input')

        new_open_page = Open_Page()
        new_open_page.text = temp
        new_open_page.save()

        return HttpResponseRedirect(reverse('accountapp:open'))
    else:
        open_page_list = Open_Page.objects.all()
        return render(request, 'accountapp/open_page.html', context={'open_page_list': open_page_list})