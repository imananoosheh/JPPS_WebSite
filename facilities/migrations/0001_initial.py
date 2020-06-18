# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-12 00:58
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=64, verbose_name='تیتر به انگلیسی')),
                ('farsi_title', models.CharField(max_length=64, verbose_name='تیتر به فارسی')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='توضیحات به انگلیسی')),
                ('farsi_description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='توضیحات به فارسی')),
            ],
            options={
                'verbose_name': 'محتوی',
                'verbose_name_plural': 'محتوی',
            },
        ),
    ]
