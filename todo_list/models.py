# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Task(models.Model):
    task_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    Description = models.CharField(max_length=500)
    time = models.DateTimeField('date to finish')