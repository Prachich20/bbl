# Generated by Django 3.0.3 on 2020-03-03 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='game',
            old_name='team',
            new_name='qualified_team',
        ),
        migrations.RemoveField(
            model_name='game',
            name='average_score',
        ),
        migrations.RemoveField(
            model_name='game',
            name='is_winner',
        ),
    ]
