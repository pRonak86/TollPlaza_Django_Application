# Generated by Django 3.1.5 on 2021-01-23 04:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Toll', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_registration',
            name='registration_Date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
    ]
