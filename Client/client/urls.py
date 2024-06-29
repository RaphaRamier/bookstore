from django.urls import path
from Client.client.views import home, analytics, balance

urlpatterns=[
    path('home/', home, name='home'),
    path('analytics/', analytics, name='analytics'),
    path('balance/', balance, name='balance')

]