# Generated by Django 5.0.2 on 2024-05-23 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chef', '0004_alter_chef_bio_alter_chef_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='chef',
            name='username',
            field=models.CharField(default=True, max_length=150),
        ),
    ]
