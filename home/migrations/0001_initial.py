# Generated by Django 3.1.2 on 2021-07-29 05:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(default='', max_length=50)),
                ('desc', models.CharField(default='', max_length=5000)),
                ('price', models.IntegerField(default=0)),
                ('image', models.ImageField(upload_to='static/image/home')),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='SearchData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickupL', models.CharField(max_length=1000)),
                ('dropL', models.CharField(max_length=1000)),
                ('drop2L', models.CharField(max_length=1000)),
                ('drop3L', models.CharField(max_length=1000)),
                ('bookingTime', models.CharField(max_length=1000)),
                ('scheduleDay', models.CharField(default='', max_length=100)),
                ('scheduleTime', models.CharField(default='', max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('slug', models.SlugField()),
            ],
        ),
    ]
