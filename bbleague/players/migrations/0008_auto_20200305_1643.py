# Generated by Django 3.0.3 on 2020-03-05 05:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0007_auto_20200305_1441'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='players',
            name='percentile',
        ),
        migrations.RemoveField(
            model_name='players',
            name='rank',
        ),
    ]
