# Generated by Django 5.0.2 on 2024-05-23 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chef', '0005_chef_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chef',
            name='username',
        ),
    ]
