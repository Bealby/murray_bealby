# Generated by Django 3.2.7 on 2023-02-23 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20230223_0452'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='crud',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
    ]
