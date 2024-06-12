from django.urls import path
from Client.client.views import test_home

urlpatterns=[
    path('', test_home, name='home')

]