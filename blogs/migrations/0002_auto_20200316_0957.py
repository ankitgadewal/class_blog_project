# Generated by Django 3.0.3 on 2020-03-16 21:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogs',
            name='datetime',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 16, 9, 57, 3, 776347)),
        ),
    ]
