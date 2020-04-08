# Generated by Django 3.0.5 on 2020-04-08 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.TextField(choices=[('moscow', 'Москва'), ('spb', 'Санкт Петербург')], default=('moscow', 'Москва'), verbose_name='Город'),
        ),
    ]
