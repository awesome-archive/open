# Generated by Django 2.2.13 on 2020-07-12 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0010_data_migration_add_demo_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="wellbeinglog",
            name="mental_value",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="wellbeinglog",
            name="physical_value",
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]
