# Generated by Django 5.0 on 2024-01-01 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ctip', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='user_password',
            new_name='password',
        ),
    ]
