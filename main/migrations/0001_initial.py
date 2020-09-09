# Generated by Django 3.1 on 2020-08-30 03:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_userforeignkey.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CareerModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified_at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted_at')),
                ('status', models.BooleanField(default=True, help_text='Status the object has currently', verbose_name='status')),
                ('name', models.CharField(help_text='Nombre de la carrera', max_length=200, verbose_name='Nombre')),
                ('code', models.CharField(help_text='Código de carrera', max_length=100, verbose_name='Código')),
                ('creator', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modifier', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Carrera',
                'verbose_name_plural': 'Carreras',
                'db_table': 'carrera',
            },
        ),
        migrations.CreateModel(
            name='ContractModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified_at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted_at')),
                ('status', models.BooleanField(default=True, help_text='Status the object has currently', verbose_name='status')),
                ('name', models.CharField(help_text='Nombres completos', max_length=200, verbose_name='Nombres')),
                ('code', models.CharField(help_text='Código referencial del contrato. Ej: COD001', max_length=10, verbose_name='Codigo')),
                ('creator', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modifier', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Contrato',
                'verbose_name_plural': 'Contratos',
                'db_table': 'contrato',
            },
        ),
        migrations.CreateModel(
            name='MeshModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified_at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted_at')),
                ('status', models.BooleanField(default=True, help_text='Status the object has currently', verbose_name='status')),
                ('name', models.CharField(help_text='Nombres completos', max_length=200, verbose_name='Nombres')),
                ('year', models.PositiveSmallIntegerField(verbose_name='Año')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='careers', to='main.careermodel', verbose_name='Carrera')),
                ('creator', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modifier', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Malla',
                'verbose_name_plural': 'Mallas',
                'db_table': 'malla',
            },
        ),
        migrations.CreateModel(
            name='TermModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified_at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted_at')),
                ('status', models.BooleanField(default=True, help_text='Status the object has currently', verbose_name='status')),
                ('name', models.CharField(help_text='Nombres completos', max_length=120, verbose_name='Nombre')),
                ('year', models.PositiveSmallIntegerField(default=2020, verbose_name='Año')),
                ('creator', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modifier', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Periodo',
                'verbose_name_plural': 'Periodos',
                'db_table': 'periodo',
            },
        ),
        migrations.CreateModel(
            name='TeacherModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified_at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted_at')),
                ('status', models.BooleanField(default=True, help_text='Status the object has currently', verbose_name='status')),
                ('full_name', models.CharField(help_text='Nombres completos', max_length=200, verbose_name='Nombres')),
                ('alias', models.CharField(help_text='Nombre referencial al profesor. Ej: CH', max_length=20, verbose_name='Alias')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='assigned_carrer', to='main.careermodel', verbose_name='Carrera')),
                ('contract', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contracts', to='main.contractmodel', verbose_name='Contrato')),
                ('creator', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modifier', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Profesor',
                'verbose_name_plural': 'Profesores',
                'db_table': 'profesor',
            },
        ),
        migrations.CreateModel(
            name='SubjectModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified_at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted_at')),
                ('status', models.BooleanField(default=True, help_text='Status the object has currently', verbose_name='status')),
                ('name', models.CharField(help_text='Nombres completos', max_length=200, verbose_name='Nombres')),
                ('code', models.CharField(help_text='Código de la materia. Ej: MAT001', max_length=50, verbose_name='Código')),
                ('creator', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modifier', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Materia',
                'verbose_name_plural': 'Materias',
                'db_table': 'materia',
            },
        ),
        migrations.CreateModel(
            name='SubjectMeshModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified_at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted_at')),
                ('status', models.BooleanField(default=True, help_text='Status the object has currently', verbose_name='status')),
                ('creator', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('mesh', models.ForeignKey(blank=True, help_text='Malla nivel', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='level', to='main.meshmodel', verbose_name='Nivel')),
                ('modifier', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('subject', models.ForeignKey(help_text='Materia.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.subjectmodel', verbose_name='Materia')),
            ],
            options={
                'db_table': 'materia_malla',
            },
        ),
        migrations.CreateModel(
            name='PlanModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created_at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified_at')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='deleted_at')),
                ('status', models.BooleanField(default=True, help_text='Status the object has currently', verbose_name='status')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.careermodel', verbose_name='Carrera')),
                ('creator', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modifier', django_userforeignkey.models.fields.UserForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('term', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.termmodel', verbose_name='Periodo')),
            ],
            options={
                'verbose_name': 'Planificación',
                'verbose_name_plural': 'Planificaciones',
                'db_table': 'planificacion',
            },
        ),
        migrations.AddField(
            model_name='meshmodel',
            name='subjects',
            field=models.ManyToManyField(through='main.SubjectMeshModel', to='main.SubjectModel'),
        ),
    ]
