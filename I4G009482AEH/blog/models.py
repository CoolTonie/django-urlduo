from getpass import getuser
from operator import mod
from sre_parse import Tokenizer
from time import timezone
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime
from django.contrib.auth import get_user_model
from django.utils.timezone import timezone

# Create your models here.
# Post

# --------

# Title : A string of maxlength 200, use Django’s models.CharField
class Title(models.Model):
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    contents=models.CharField(max_length=500)
    
 
# Text : Any amount of text, use Django’s TextField
class Text(models.Model):
    body=models.CharField(max_length=2000)
     
# Author : A Foreign Key to the current user model. Make use of Django’s get_user_model function.
class Author(models.Model):
    name=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    first_name= models.CharField(max_length=50)
    last_name= models.CharField(max_length=50)
 
# Created_date : A date-time column, use Django’s models.DateTimeField. 
class Created_date(models.Model):
    date=models.DateTimeField(default=datetime.date)
    time=models.DateTimeField(auto_now=True)
 
# Published_date : A date-time column, use Django’s models.DateTimeField. 
class Published_date(models.Model):
    date=models.DateTimeField(default=datetime.date)
    time=models.DateTimeField(auto_now=True)




    