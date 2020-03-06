# Generated by Django 3.0.3 on 2020-03-05 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0006_players_height'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='percentile',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AddField(
            model_name='players',
            name='rank',
            field=models.IntegerField(default=0),
        ),
    ]
