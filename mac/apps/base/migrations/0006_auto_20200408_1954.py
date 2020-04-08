# Generated by Django 3.0.5 on 2020-04-08 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_user_is_stuff'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='is_stuff',
        ),
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='staff status'),
        ),
    ]
