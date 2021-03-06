# -*- coding: utf-8 -*-
# Generated by Django 1.9.3 on 2016-03-08 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='alternate_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='tagline',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
