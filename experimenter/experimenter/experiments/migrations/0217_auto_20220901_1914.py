# Generated by Django 3.2.15 on 2022-09-01 19:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0216_nimbusexperiment_is_first_run"),
    ]

    operations = [
        migrations.AddField(
            model_name="nimbusexperiment",
            name="_end_date",
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="nimbusexperiment",
            name="_start_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
