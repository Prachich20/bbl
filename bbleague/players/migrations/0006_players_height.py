# Generated by Django 3.0.3 on 2020-03-04 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0005_auto_20200304_0915'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='height',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]
