# Generated by Django 3.2.7 on 2023-02-23 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True,
                                           serialize=False,
                                           verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=254,
                                          null=True)),
                ('description_1', models.TextField(blank=True,
                                                   max_length=1000,
                                                   null=True)),
                ('description_2', models.TextField(blank=True, max_length=1000,
                                                   null=True)),
                ('hobbie_1', models.TextField(blank=True, max_length=1000,
                                              null=True)),
                ('hobbie_2', models.TextField(blank=True, max_length=1000,
                                              null=True)),
                ('hobbie_3', models.TextField(blank=True, max_length=1000,
                                              null=True)),
                ('hobbie_4', models.TextField(blank=True, max_length=1000,
                                              null=True)),
            ],
        ),
    ]
