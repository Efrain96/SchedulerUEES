# Generated by Django 3.1.1 on 2020-09-08 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20200907_2316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineitemschedulemodel',
            name='end_time',
            field=models.CharField(blank=True, help_text='Hora fin', max_length=70, null=True, verbose_name='Hora fin'),
        ),
        migrations.AlterField(
            model_name='lineitemschedulemodel',
            name='start_time',
            field=models.CharField(blank=True, help_text='Hora inicio', max_length=70, null=True, verbose_name='Hora inicio'),
        ),
    ]
