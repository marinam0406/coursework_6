# Generated by Django 5.0.6 on 2024-06-15 19:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailingsettings',
            options={'verbose_name': 'Настройка рассылки', 'verbose_name_plural': 'Настройки рассылок'},
        ),
    ]
