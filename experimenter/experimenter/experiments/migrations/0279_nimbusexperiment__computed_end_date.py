# Generated by Django 5.1.5 on 2025-02-26 05:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0278_alter_nimbusexperiment_qa_status"),
    ]

    operations = [
        migrations.AddField(
            model_name="nimbusexperiment",
            name="_computed_end_date",
            field=models.DateField(
                blank=True, null=True, verbose_name="Computed End Date"
            ),
        ),
    ]
