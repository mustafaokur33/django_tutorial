from turtle import title
from unittest.util import _MAX_LENGTH
from django.db import models


class Noes(models.Model):
    title  =models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

