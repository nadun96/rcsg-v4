# Generated by Django 4.0 on 2023-01-04 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_memberrole_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberrole',
            name='role',
            field=models.IntegerField(blank=True, choices=[(3, 'Secretary'), (2, 'Member'), (1, 'Admin'), (4, 'Storekeeper')]),
        ),
    ]
