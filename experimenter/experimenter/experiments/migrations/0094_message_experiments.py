# Generated by Django 3.0.5 on 2020-04-23 21:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0093_experiment_windows_versions"),
    ]

    operations = [
        migrations.AddField(
            model_name="experiment",
            name="message_template",
            field=models.CharField(
                blank=True,
                choices=[
                    ("cfr_doorhanger", "CFR Doorhanger"),
                    ("cfr_urlbar_chiclet", "CFR Urlbar Chiclet"),
                    ("milestone_message", "Milestone Message"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="experiment",
            name="message_type",
            field=models.CharField(
                blank=True,
                choices=[("cfr", "CFR"), ("about:welcome", "about:welcome")],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="experimentvariant",
            name="message_targeting",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="experimentvariant",
            name="message_threshold",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="experimentvariant",
            name="message_triggers",
            field=models.TextField(blank=True, null=True),
        ),
    ]
