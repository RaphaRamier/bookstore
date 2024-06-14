from django.urls import path
from Client.client.views import home

urlpatterns=[
    path('home/', home, name='home')

]