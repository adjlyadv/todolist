# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='todothing',
            fields=[
                ('task_id', models.AutoField(serialize=False, primary_key=True)),
                ('task_introduction', models.TextField(default=b' ', max_length=300)),
                ('task_createtime', models.DateTimeField(auto_now_add=True)),
                ('task_isfinshed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-task_createtime',),
            },
        ),
    ]
