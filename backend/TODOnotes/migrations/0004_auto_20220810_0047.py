# Generated by Django 3.2.14 on 2022-08-09 21:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TODOnotes', '0003_auto_20220802_2314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='user_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='age',
        ),
        migrations.RemoveField(
            model_name='user',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='user',
            name='password',
        ),
    ]
