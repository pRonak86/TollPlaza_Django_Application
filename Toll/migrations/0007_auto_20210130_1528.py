# Generated by Django 3.1.5 on 2021-01-30 09:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Toll', '0006_ewallet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ewallet',
            name='cust_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Toll.customer_registration'),
        ),
    ]
