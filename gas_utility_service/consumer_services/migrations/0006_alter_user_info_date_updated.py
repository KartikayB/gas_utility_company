# Generated by Django 4.2.4 on 2023-08-13 06:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('consumer_services', '0005_user_info_updated_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='date_updated',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
