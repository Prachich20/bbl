# Generated by Django 3.0.3 on 2020-03-03 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20200303_1215'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='is_coach',
            field=models.BooleanField(default=False),
        ),
    ]