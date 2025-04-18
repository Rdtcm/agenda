from django.db import models
from django.utils import timezone

# Create your models here.

'''
MODELS:

# id (primary key) --> criado automaticamente pelo django

first_name(string), last_name(string), phone(string), 
category(foreign key), email(email), picture(imagem), 
owner(foreign key), created_date(date), show(boolean), 
description(text)

'''

class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=250, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    
