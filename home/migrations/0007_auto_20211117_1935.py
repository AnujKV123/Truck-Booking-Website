# Generated by Django 3.1.2 on 2021-11-17 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_bookingrate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookingrate',
            old_name='max',
            new_name='Rate',
        ),
        migrations.RenameField(
            model_name='bookingrate',
            old_name='medium',
            new_name='Truck_Type',
        ),
        migrations.RemoveField(
            model_name='bookingrate',
            name='micro',
        ),
        migrations.RemoveField(
            model_name='bookingrate',
            name='mini',
        ),
        migrations.RemoveField(
            model_name='bookingrate',
            name='ultramax',
        ),
    ]
