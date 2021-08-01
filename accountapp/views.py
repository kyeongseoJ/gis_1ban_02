from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

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


class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:open')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'


class AccountUpdateView(UpdateView):
    model = User
    form_class = UserCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:open')
    template_name = 'accountapp/update.html'







