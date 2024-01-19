# surveys/models.py
from django.db import models

class Survey(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    question = models.CharField(max_length=255)  # Add this line

    def __str__(self):
        return self.title

class Response(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    birthdate = models.DateField()
    about_yourself = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
