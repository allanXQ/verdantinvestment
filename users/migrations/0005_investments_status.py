# Generated by Django 4.0.6 on 2022-11-25 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_affiliate_username_alter_deposits_username_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='investments',
            name='STATUS',
            field=models.CharField(default='pending', max_length=10, null=True),
        ),
    ]