# Generated by Django 3.0.3 on 2020-03-17 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0003_auto_20200316_2108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 16, 21, 10, 56, 821126)),
        ),
    ]
