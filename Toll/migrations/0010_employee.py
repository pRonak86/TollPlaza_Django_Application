# Generated by Django 3.1.5 on 2021-02-06 07:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Toll', '0009_auto_20210203_1451'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('e_fname', models.CharField(max_length=20)),
                ('e_lname', models.CharField(max_length=20)),
                ('e_contact', models.IntegerField()),
                ('e_email', models.EmailField(max_length=254)),
                ('e_gender', models.CharField(max_length=20)),
                ('e_bod', models.DateField()),
                ('e_jod', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('e_bloodGroup', models.CharField(max_length=20)),
                ('e_City', models.CharField(max_length=20)),
                ('e_State', models.CharField(max_length=20)),
                ('e_Coutry', models.CharField(max_length=20)),
                ('e_empCode', models.CharField(editable=False, max_length=10, primary_key=True, serialize=False, unique=True)),
                ('e_password', models.CharField(max_length=20)),
            ],
        ),
    ]