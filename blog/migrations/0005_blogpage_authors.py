# Generated by Django 5.1.5 on 2025-01-21 13:54

import modelcluster.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='authors',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='blog.author'),
        ),
    ]
