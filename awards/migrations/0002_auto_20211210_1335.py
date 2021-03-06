# Generated by Django 3.2.9 on 2021-12-10 13:35

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('project_name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=2000)),
                ('category', models.TextField(max_length=20)),
                ('location', models.TextField(max_length=20)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.RemoveField(
            model_name='picture',
            name='category',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='location',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Location',
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
    ]
