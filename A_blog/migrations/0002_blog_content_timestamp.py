# Generated by Django 3.1.2 on 2021-01-19 17:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('A_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog_content',
            name='timeStamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
