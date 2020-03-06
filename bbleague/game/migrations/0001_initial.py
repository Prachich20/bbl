# Generated by Django 3.0.3 on 2020-03-03 02:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('team', '0002_team_is_winner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('round', models.CharField(choices=[(0, 'Round_0'), (1, 'Round_1'), (2, 'Round_2'), (3, 'Round_3'), (4, 'Round_4')], default=0, max_length=1)),
                ('average_score', models.IntegerField(default=0)),
                ('is_winner', models.BooleanField(default=False)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.Team')),
            ],
        ),
    ]
