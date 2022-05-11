# Generated by Django 3.1.5 on 2021-01-21 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=20)),
                ('lname', models.CharField(max_length=20)),
                ('contact', models.IntegerField(max_length=10)),
                ('emailid', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=20)),
                ('vehicalNo', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('registration_Date', models.DateField()),
                ('account', models.CharField(default='deactive', max_length=20)),
            ],
        ),
    ]
