# Generated by Django 4.2.20 on 2025-04-11 18:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('autenticacao', '0002_alter_pessoa_user_inclusao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Escolas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('dt_edicao', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
                ('diretor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='escolas_diretor', to='autenticacao.pessoa')),
                ('user_edicao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_edicao', to=settings.AUTH_USER_MODEL)),
                ('user_inclusao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_inclusao', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Nivel_Ensino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('dt_edicao', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
                ('user_edicao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_edicao', to=settings.AUTH_USER_MODEL)),
                ('user_inclusao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_inclusao', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Turmas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('dt_edicao', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
                ('ano', models.IntegerField(verbose_name='Ano de atuação da turma')),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turmas', to='educacao.escolas')),
                ('nivel_ensino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='turmas', to='educacao.nivel_ensino')),
                ('user_edicao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_edicao', to=settings.AUTH_USER_MODEL)),
                ('user_inclusao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_inclusao', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tipo_Avaliacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('dt_edicao', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
                ('arquivo', models.FileField(upload_to='avaliacoes/')),
                ('user_edicao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_edicao', to=settings.AUTH_USER_MODEL)),
                ('user_inclusao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_inclusao', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Avaliacoes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('dt_edicao', models.DateTimeField(auto_now=True)),
                ('ano', models.IntegerField(verbose_name='Ano de realização da avaliação')),
                ('semestre', models.IntegerField(verbose_name='Semestre de realização da avaliação')),
                ('nivel_ensino', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='educacao.nivel_ensino')),
                ('tipo_avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avaliacoes', to='educacao.tipo_avaliacoes')),
                ('user_edicao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_edicao', to=settings.AUTH_USER_MODEL)),
                ('user_inclusao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_inclusao', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Alunos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_inclusao', models.DateTimeField(auto_now_add=True)),
                ('dt_edicao', models.DateTimeField(auto_now=True)),
                ('nome', models.CharField(max_length=100)),
                ('escola', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alunos', to='educacao.escolas')),
                ('user_edicao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_edicao', to=settings.AUTH_USER_MODEL)),
                ('user_inclusao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_inclusao', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
