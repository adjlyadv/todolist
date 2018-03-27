# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Todolist',
            fields=[
                ('task_id', models.AutoField(serialize=False, primary_key=True)),
                ('task_introduction', models.TextField(default=b' ', max_length=300)),
                ('task_isfinshed', models.BooleanField(default=False)),
                ('task_createtime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-task_createtime',),
            },
        ),
        migrations.DeleteModel(
            name='todothing',
        ),
    ]
