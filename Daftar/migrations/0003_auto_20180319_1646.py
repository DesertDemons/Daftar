# Generated by Django 2.0.3 on 2018-03-19 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Daftar', '0002_remove_profile_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='Profile',
            new_name='profile',
        ),
    ]
