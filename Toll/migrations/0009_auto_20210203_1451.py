# Generated by Django 3.1.5 on 2021-02-03 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Toll', '0008_auto_20210202_1253'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_registration',
            name='deactivation_Date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='customer_registration',
            name='account',
            field=models.CharField(default='Deactive', max_length=20),
        ),
    ]
