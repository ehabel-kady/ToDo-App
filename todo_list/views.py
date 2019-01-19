# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

# Create your views here.
def index(request):
    task_list = Task.objects.order_by('task_id')
    output = '\n'.join([task.name for task in task_list])
    print(output)
    return HttpResponse(output)

def task(request, task_id):
    return HttpResponse('This will get the task details')
