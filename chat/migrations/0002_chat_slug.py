# Generated by Django 2.2.28 on 2023-03-04 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chat',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]
