# Generated by Django 3.2.7 on 2023-02-20 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_project_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='image_mockup',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
