# Generated by Django 3.1.1 on 2020-09-07 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20200906_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeavailabilitymodel',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Descripcion'),
        ),
    ]
