# Generated by Django 3.1.7 on 2021-03-27 11:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simple_backend_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='inventory_count',
            field=models.BigIntegerField(default=0),
        ),
    ]
