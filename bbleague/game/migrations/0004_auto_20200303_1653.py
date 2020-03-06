# Generated by Django 3.0.3 on 2020-03-03 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_game_is_final'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='round',
            field=models.CharField(choices=[('0', 'Round_0'), ('1', 'Round_1'), ('2', 'Round_2'), ('3', 'Round_3'), ('4', 'Round_4')], default='0', max_length=1),
        ),
    ]
