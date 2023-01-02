# Generated by Django 4.0 on 2022-12-31 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_memberrole_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberrole',
            name='role',
            field=models.IntegerField(blank=True, choices=[(1, 'Admin'), (2, 'Member'), (3, 'Secretary'), (4, 'Storekeeper')]),
        ),
    ]
