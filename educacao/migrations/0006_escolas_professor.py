# Generated by Django 4.2.20 on 2025-04-29 19:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autenticacao', '0002_alter_pessoa_user_inclusao'),
        ('educacao', '0005_remove_tipo_avaliacoes_arquivo_avaliacoes_arquivo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='escolas',
            name='professor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='escolas_professor', to='autenticacao.pessoa'),
        ),
    ]
