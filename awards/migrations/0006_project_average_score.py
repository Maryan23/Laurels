# Generated by Django 3.2.9 on 2021-12-13 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0005_rename_avg_rate_rating_average'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='average_score',
            field=models.FloatField(default=0),
        ),
    ]
