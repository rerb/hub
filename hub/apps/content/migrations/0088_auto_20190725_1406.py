# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-07-25 14:06
from __future__ import unicode_literals

from django.db import migrations
import s3direct.fields


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0087_auto_20190117_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='item',
            field=s3direct.fields.S3DirectField(blank=True, help_text='Valid formats are acceptable: PDF, Excel, Word, PPT', null=True),
        ),
    ]