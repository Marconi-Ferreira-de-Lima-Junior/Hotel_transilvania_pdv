from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Painel admin do Django
    path('', include('pdv.urls')),
]
