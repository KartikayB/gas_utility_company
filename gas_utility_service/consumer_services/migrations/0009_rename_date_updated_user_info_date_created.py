# Generated by Django 4.2.4 on 2023-08-13 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('consumer_services', '0008_alter_user_info_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_info',
            old_name='date_updated',
            new_name='date_created',
        ),
    ]