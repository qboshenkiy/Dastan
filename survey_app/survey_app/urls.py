# survey_app/urls.py
from django.contrib import admin
# survey_app/urls.py
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('surveys/', include('surveys.urls')),
    path('', include('surveys.urls')),  # Добавьте эту строку
]
