# Generated by Django 4.1.5 on 2023-01-28 12:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='work_from_home',
            new_name='price',
        ),
    ]
