from django.urls import path
from Client.user.views import loginpage, logout
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('login/', loginpage, name='login'),
    path('logout/', logout, name='logout')

]