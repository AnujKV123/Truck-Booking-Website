# Generated by Django 3.1.2 on 2021-08-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trucklocation',
            name='TruckType',
            field=models.CharField(default=0, max_length=300),
        ),
        migrations.AddField(
            model_name='trucklocation',
            name='Truck_Desc',
            field=models.CharField(default=0, max_length=1000),
        ),
    ]
