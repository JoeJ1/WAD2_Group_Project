# Generated by Django 2.2.28 on 2023-03-10 19:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0016_auto_20230310_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time_stamp',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 10, 19, 45, 17, 566888, tzinfo=utc)),
        ),
    ]
