# Generated by Django 4.2.20 on 2025-05-05 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('educacao', '0008_alunos_avaliacao1_alunos_avaliacao2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alunos',
            name='detalhe',
            field=models.CharField(default='Nenhum detalhe declarado.', max_length=500),
        ),
    ]
