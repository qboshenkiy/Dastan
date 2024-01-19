# surveys/urls.py
from django.urls import path
from .views import survey_detail, survey_list, success

urlpatterns = [
    path('', survey_list, name='survey_list'),
    path('<int:survey_id>/', survey_detail, name='survey_detail'),
    path('success/', success, name='success'),  # Добавьте этот маршрут
]
