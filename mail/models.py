from django.db import models

# Create your models here.

class Mail(models.Model):
    to = models.CharField(max_length=30)
    sender = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    body = models.CharField(max_length=1000)
    password = models.CharField(max_length=20)