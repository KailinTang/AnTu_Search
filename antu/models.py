from django.db import models

# Create your models here.
from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render_to_response


class Post(models.Model):
    img=models.ImageField(null=True,upload_to='antu/static/pic')