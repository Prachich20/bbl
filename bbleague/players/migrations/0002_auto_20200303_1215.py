# Generated by Django 3.0.3 on 2020-03-03 01:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='players',
            name='average_score',
        ),
        migrations.RemoveField(
            model_name='players',
            name='is_winner',
        ),
    ]
