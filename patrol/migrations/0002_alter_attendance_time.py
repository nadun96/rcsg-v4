# Generated by Django 4.0 on 2023-01-04 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patrol', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='time',
            field=models.TimeField(auto_now_add=True),
        ),
    ]
