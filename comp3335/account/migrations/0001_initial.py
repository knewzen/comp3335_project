# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-05 15:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=255, unique=True)),
                ('pwd_hash', models.CharField(max_length=255)),
                ('salt1', models.CharField(max_length=255)),
                ('salt2', models.CharField(max_length=255)),
                ('f_name', models.CharField(max_length=90)),
                ('l_name', models.CharField(max_length=90)),
                ('age', models.CharField(max_length=64)),
            ],
        ),
    ]
