# Generated by Django 3.0.3 on 2020-03-16 08:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blogs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=500)),
                ('datetime', models.DateTimeField(blank=True, default=datetime.datetime(2020, 3, 15, 20, 3, 59, 204156))),
            ],
        ),
    ]
