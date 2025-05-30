# Generated by Django 3.2.5 on 2021-11-10 15:27

import django.db.models.deletion
from django.db import migrations, models


def migrate_feature_configs(apps, schema_editor):
    NimbusExperiment = apps.get_model("experiments", "NimbusExperiment")
    NimbusBranchFeatureValue = apps.get_model("experiments", "NimbusBranchFeatureValue")

    for experiment in NimbusExperiment.objects.all():
        if experiment.feature_config:
            experiment.feature_configs.add(experiment.feature_config)

        for branch in experiment.branches.all():
            NimbusBranchFeatureValue.objects.create(
                branch=branch,
                feature_config=experiment.feature_config,
                enabled=branch.feature_enabled,
                value=branch.feature_value,
            )


class Migration(migrations.Migration):
    dependencies = [
        ("experiments", "0197_auto_20211109_2000"),
    ]

    operations = [
        migrations.AddField(
            model_name="nimbusexperiment",
            name="feature_configs",
            field=models.ManyToManyField(
                blank=True, to="experiments.NimbusFeatureConfig"
            ),
        ),
        migrations.CreateModel(
            name="NimbusBranchFeatureValue",
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
                ("enabled", models.BooleanField(default=True)),
                ("value", models.TextField(blank=True, null=True)),
                (
                    "branch",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="feature_values",
                        to="experiments.nimbusbranch",
                    ),
                ),
                (
                    "feature_config",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="experiments.nimbusfeatureconfig",
                    ),
                ),
            ],
            options={
                "verbose_name": "Nimbus Branch Feature Value",
                "verbose_name_plural": "Nimbus Branch Feature Values",
            },
        ),
        migrations.AddConstraint(
            model_name="nimbusbranchfeaturevalue",
            constraint=models.UniqueConstraint(
                condition=models.Q(("feature_config__isnull", False)),
                fields=("branch", "feature_config"),
                name="unique_with_branch_and_feature",
            ),
        ),
        migrations.RunPython(migrate_feature_configs),
        migrations.RemoveField(
            model_name="nimbusbranch",
            name="feature_enabled",
        ),
        migrations.RemoveField(
            model_name="nimbusbranch",
            name="feature_value",
        ),
        migrations.RemoveField(
            model_name="nimbusexperiment",
            name="feature_config",
        ),
    ]
