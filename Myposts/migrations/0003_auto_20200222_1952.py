# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2020-02-22 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Myposts', '0002_event_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='Image',
            field=models.ImageField(default='Null', upload_to='images/'),
        ),
    ]
