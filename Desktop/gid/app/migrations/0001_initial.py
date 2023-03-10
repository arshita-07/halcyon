# Generated by Django 4.1.5 on 2023-01-28 11:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20230119_2011'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medical_history', models.FileField(upload_to='medical_history')),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant', to='users.clientuser')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('resource_description', models.TextField()),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('keywords', models.CharField(default='NA', max_length=200)),
                ('status', models.BooleanField(default=False)),
                ('quantity', models.TextField()),
                ('available_deadline', models.DateField(null=True, verbose_name='Available till')),
                ('location', models.CharField(default='work from home only', max_length=300)),
                ('work_from_home', models.CharField(default='0', max_length=200)),
                ('applicants', models.ManyToManyField(related_name='applicants', through='app.Application', to='users.clientuser')),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospital', to='users.hospital')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='resource', to='app.resource'),
        ),
    ]
