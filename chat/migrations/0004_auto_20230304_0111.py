# Generated by Django 2.2.28 on 2023-03-04 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20230304_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chat',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]
