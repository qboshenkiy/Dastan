# surveys/admin.py
from django.contrib import admin
from .models import Survey, Response

admin.site.register(Survey)
admin.site.register(Response)
