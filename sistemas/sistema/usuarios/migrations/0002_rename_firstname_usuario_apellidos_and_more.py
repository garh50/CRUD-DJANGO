# Generated by Django 4.1.7 on 2023-02-26 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='firstname',
            new_name='Apellidos',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='birthdate',
            new_name='Nacimiento',
        ),
        migrations.RenameField(
            model_name='usuario',
            old_name='lastname',
            new_name='Nombres',
        ),
    ]
