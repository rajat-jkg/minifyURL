from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class urls(models.Model):
    Name = models.CharField(max_length=100 , blank=True)  
    slug = models.CharField(max_length=6 ,  unique=True) 
    url = models.URLField(max_length=1500)
    user_id = models.IntegerField(default=-1 , blank=True) 

class visits(models.Model):
    url = models.ForeignKey(urls , on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now_add=True)
