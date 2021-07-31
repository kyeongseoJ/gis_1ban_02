from django.urls import path

from accountapp.views import open_page

app_name = 'accountapp'

urlpatterns = [
    path('open/',open_page , name='open')
]