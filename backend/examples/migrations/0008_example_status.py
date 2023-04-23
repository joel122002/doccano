# Generated by Django 4.1.7 on 2023-04-23 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("examples", "0007_example_score"),
    ]

    operations = [
        migrations.AddField(
            model_name="example",
            name="status",
            field=models.CharField(
                choices=[("not_started", "Not Started"), ("in_progress", "In Progress"), ("finished", "Finished")],
                default="not_started",
                max_length=11,
            ),
        ),
    ]
