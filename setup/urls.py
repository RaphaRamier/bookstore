from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('genres.urls')),
    path('', include('authors.urls')),
    path('', include('assembly.urls')),
    path('', include('books.urls')),
    path('', include('suppliers.urls')),
    path('', include('components.urls')),

]
