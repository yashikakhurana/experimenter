# Generated by Django 2.1.2 on 2019-01-10 21:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [("experiments", "0025_auto_20190107_2241")]

    operations = [
        migrations.AddField(
            model_name="experiment",
            name="qa_status",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="experiment",
            name="risk_technical",
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name="experiment",
            name="risk_technical_description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="experiment",
            name="test_builds",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="experiment",
            name="testing",
            field=models.TextField(blank=True, null=True),
        ),
    ]
