# Generated by Django 3.2.18 on 2023-04-24 21:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0230_alter_nimbusbranchfeaturevalue_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="nimbusexperiment",
            name="proposed_release_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]
