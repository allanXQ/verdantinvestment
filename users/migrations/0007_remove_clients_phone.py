# Generated by Django 4.0.6 on 2022-11-25 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_rename_status_investments_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clients',
            name='phone',
        ),
    ]
