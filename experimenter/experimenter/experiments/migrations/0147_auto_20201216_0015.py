# Generated by Django 3.1.3 on 2020-12-16 00:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0146_auto_20201215_1624"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nimbusbranch",
            name="description",
            field=models.TextField(blank=True, default=""),
        ),
    ]
