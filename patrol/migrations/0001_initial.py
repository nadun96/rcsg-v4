# Generated by Django 4.0 on 2023-01-04 05:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0006_alter_memberrole_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now_add=True)),
                ('time', models.TimeField()),
                ('marker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marker', to='core.profile')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='member', to='core.profile')),
            ],
        ),
    ]
