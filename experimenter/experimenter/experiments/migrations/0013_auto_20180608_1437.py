# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-08 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("experiments", "0012_experiment_analysis_owner")]

    operations = [
        migrations.AddField(
            model_name="experiment",
            name="bugzilla_id",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="analysis",
            field=models.TextField(
                blank=True,
                default="What is the main effect you are looking for and what data will\nyou use to make these decisions? What metrics are you using to measure success\n\nDo you plan on surveying users at the end of the study? Yes/No.\nStrategy and Insights can help create surveys if needed\n    ",
                null=True,
            ),
        ),
    ]
