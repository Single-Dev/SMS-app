# Generated by Django 4.2.4 on 2023-10-21 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='facebook',
        ),
    ]
