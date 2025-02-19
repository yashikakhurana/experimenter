# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-20 22:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("experiments", "0002_auto_20171115_1918")]

    operations = [
        migrations.AlterField(
            model_name="experiment",
            name="client_matching",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="pref_branch",
            field=models.CharField(
                choices=[("default", "default"), ("user", "user")],
                default="default",
                max_length=255,
            ),
        ),
    ]
