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
class post(models.Model):
    title=models.CharField(max_length=200)
    Text=models.CharField(max_length=2000)
    Author=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Created_date=models.DateTimeField(auto_now=True)
    Published_date=models.DateTimeField(auto_now=True)


def _str_(self):
    return self.text

    