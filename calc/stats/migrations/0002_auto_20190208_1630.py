# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2019-02-08 15:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_upload',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
