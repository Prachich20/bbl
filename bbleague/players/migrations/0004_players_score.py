# Generated by Django 3.0.3 on 2020-03-03 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0003_players_is_coach'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='score',
            field=models.IntegerField(default=0, max_length=20),
        ),
    ]
