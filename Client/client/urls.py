from django.urls import path
from Client.client.views import home, analytics

urlpatterns=[
    path('home/', home, name='home'),
    path('analytics/', analytics, name='analytics')

]