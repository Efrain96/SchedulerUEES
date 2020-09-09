# Generated by Django 3.1.1 on 2020-09-01 20:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200901_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parallelmodel',
            name='subject',
        ),
        migrations.AddField(
            model_name='parallelmodel',
            name='classroom',
            field=models.ForeignKey(blank=True, help_text='Selecciona aula.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='class_parallels', to='main.classroommodel', verbose_name='Aula'),
        ),
        migrations.AddField(
            model_name='parallelmodel',
            name='code',
            field=models.CharField(blank=True, help_text='Codigo referencial del paralelo. Opcional', max_length=20, null=True, verbose_name='Codigo'),
        ),
        migrations.AddField(
            model_name='parallelmodel',
            name='subject_mesh',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='parallels_subject_mesh', to='main.subjectmeshmodel', verbose_name='Materia Malla'),
        ),
        migrations.AlterField(
            model_name='parallelmodel',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_parallels', to='main.teachermodel', verbose_name='Profesor'),
        ),
    ]
