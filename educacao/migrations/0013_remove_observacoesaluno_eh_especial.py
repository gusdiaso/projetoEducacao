# Generated by Django 4.2.20 on 2025-05-06 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educacao', '0012_remove_resultado_avaliacoes_aprovado_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observacoesaluno',
            name='eh_especial',
        ),
    ]
