# Generated by Django 3.1.5 on 2021-01-27 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Toll', '0003_customer_registration_qr_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer_registration',
            name='activation_Date',
            field=models.DateField(null=True),
        ),
    ]
