# Generated by Django 3.0.3 on 2020-03-03 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20200303_1344'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_final',
            field=models.BooleanField(default=False),
        ),
    ]
