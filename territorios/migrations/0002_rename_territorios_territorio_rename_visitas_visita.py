# Generated by Django 5.0.4 on 2024-05-23 16:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('territorios', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Territorios',
            new_name='Territorio',
        ),
        migrations.RenameModel(
            old_name='Visitas',
            new_name='Visita',
        ),
    ]
