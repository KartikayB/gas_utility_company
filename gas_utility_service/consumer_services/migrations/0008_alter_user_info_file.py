# Generated by Django 4.2.4 on 2023-08-13 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumer_services', '0007_alter_user_info_admin_note'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_info',
            name='file',
            field=models.FileField(blank=True, upload_to=''),
        ),
    ]