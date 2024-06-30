from django.urls import path
from Client.user.views import loginpage, logout

urlpatterns = [
    path('login/', loginpage, name='login'),
    path('logout/', logout, name='logout')

]