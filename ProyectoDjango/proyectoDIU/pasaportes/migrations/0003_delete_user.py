# Generated by Django 4.0.4 on 2022-06-15 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pasaportes', '0002_user_delete_usuario'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
