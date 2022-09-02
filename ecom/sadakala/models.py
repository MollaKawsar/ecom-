from pickle import TRUE
from unicodedata import name
from django.db import models
from django.contrib.auth.models import User

class Customer (models.Model):
    user=models.OneToOneField(User,null=True,on_delete=models.CASCADE,blank=True)
    name=models.CharField(max_length=200,null=True)
    Email=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

