# Generated by Django 5.0.2 on 2024-05-23 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chef', '0006_remove_chef_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(upload_to='chef/images/'),
        ),
    ]