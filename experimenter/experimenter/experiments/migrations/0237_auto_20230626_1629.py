# Generated by Django 3.2.19 on 2023-06-26 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("experiments", "0236_alter_nimbusdocumentationlink_title"),
    ]

    operations = [
        migrations.AlterField(
            model_name="nimbusexperiment",
            name="application",
            field=models.CharField(
                choices=[
                    ("firefox-desktop", "Firefox Desktop"),
                    ("fenix", "Firefox for Android (Fenix)"),
                    ("ios", "Firefox for iOS"),
                    ("focus-android", "Focus for Android"),
                    ("klar-android", "Klar for Android"),
                    ("focus-ios", "Focus for iOS"),
                    ("klar-ios", "Klar for iOS"),
                    ("pocket-web", "Pocket Web"),
                ],
                max_length=255,
            ),
        ),
        migrations.AlterField(
            model_name="nimbusfeatureconfig",
            name="application",
            field=models.CharField(
                blank=True,
                choices=[
                    ("firefox-desktop", "Firefox Desktop"),
                    ("fenix", "Firefox for Android (Fenix)"),
                    ("ios", "Firefox for iOS"),
                    ("focus-android", "Focus for Android"),
                    ("klar-android", "Klar for Android"),
                    ("focus-ios", "Focus for iOS"),
                    ("klar-ios", "Klar for iOS"),
                    ("pocket-web", "Pocket Web"),
                ],
                max_length=255,
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="nimbusisolationgroup",
            name="application",
            field=models.CharField(
                choices=[
                    ("firefox-desktop", "Firefox Desktop"),
                    ("fenix", "Firefox for Android (Fenix)"),
                    ("ios", "Firefox for iOS"),
                    ("focus-android", "Focus for Android"),
                    ("klar-android", "Klar for Android"),
                    ("focus-ios", "Focus for iOS"),
                    ("klar-ios", "Klar for iOS"),
                    ("pocket-web", "Pocket Web"),
                ],
                max_length=255,
            ),
        ),
    ]
