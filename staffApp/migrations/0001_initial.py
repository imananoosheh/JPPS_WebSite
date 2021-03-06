# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-12 00:58
from __future__ import unicode_literals

from django.db import migrations, models
import staffApp.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='نام به انگلیسی')),
                ('farsiName', models.CharField(max_length=64, verbose_name='نام به فارسی')),
            ],
            options={
                'verbose_name': 'بخش',
                'verbose_name_plural': 'بخش',
            },
        ),
        migrations.CreateModel(
            name='person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farsiName', models.CharField(max_length=64, verbose_name='نام به فارسی')),
                ('name', models.CharField(max_length=64, verbose_name='نام به انگلیسی')),
                ('description', models.TextField(max_length=200, verbose_name='توضیحات به انگلیسی')),
                ('farsiDescription', models.TextField(max_length=200, verbose_name='توضیحات به فارسی')),
                ('avatar', models.ImageField(upload_to='staff/', validators=[staffApp.validators.validate_file_extension_avatarImage], verbose_name='عکس')),
                ('Link', models.CharField(max_length=140, verbose_name='لینک های شخصی')),
                ('category', models.ManyToManyField(to='staffApp.category', verbose_name='بخش')),
            ],
            options={
                'verbose_name': 'کارمند',
                'verbose_name_plural': 'کارکنان',
            },
        ),
    ]
