# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-19 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='id',
        ),
        migrations.AddField(
            model_name='task',
            name='task_id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='time',
            field=models.DateTimeField(verbose_name='date to finish'),
        ),
    ]
