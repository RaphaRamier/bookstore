from django.urls import path
from Client.user.views import loginpage

urlpatterns = [
    path('login/', loginpage, name='login')

]