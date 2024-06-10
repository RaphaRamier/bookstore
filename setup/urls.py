from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('API/', include('API.genres.urls')),
    path('API/', include('API.authors.urls')),
    path('API/', include('API.assembly.urls')),
    path('API/', include('API.books.urls')),
    path('API/', include('API.suppliers.urls')),
    path('API/', include('API.components.urls')),
    path('API/', include('API.sales.urls')),
    path('API/', include('API.services.urls')),
    path('API/', include('API.cashflow.urls'))

]
