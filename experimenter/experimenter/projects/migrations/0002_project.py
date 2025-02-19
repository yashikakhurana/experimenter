# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-15 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [("projects", "0001_initial")]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(max_length=255, unique=True)),
            ],
            options={"verbose_name_plural": "Projects", "verbose_name": "Project"},
        )
    ]
