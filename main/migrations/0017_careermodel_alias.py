# Generated by Django 3.1.1 on 2020-09-07 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_teachermodel_afinity'),
    ]

    operations = [
        migrations.AddField(
            model_name='careermodel',
            name='alias',
            field=models.CharField(blank='', default='', help_text='Campo referencial ej: C-2020.', max_length=50, null='', verbose_name='Alias'),
        ),
    ]