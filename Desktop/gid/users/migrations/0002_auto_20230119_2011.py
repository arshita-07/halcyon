# Generated by Django 3.1.4 on 2023-01-19 14:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='is_Hospital',
            new_name='is_Hospital',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='is_client',
            new_name='is_Client',
        ),
        migrations.AlterField(
            model_name='Hospital',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Hospital_user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='clientuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Client_user', to=settings.AUTH_USER_MODEL),
        ),
    ]