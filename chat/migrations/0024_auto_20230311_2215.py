# Generated by Django 2.2.28 on 2023-03-11 22:15

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0023_auto_20230311_1326'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 11, 22, 15, 8, 24745, tzinfo=utc)),
        ),
    ]
