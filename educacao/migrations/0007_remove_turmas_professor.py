# Generated by Django 4.2.20 on 2025-04-29 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('educacao', '0006_escolas_professor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turmas',
            name='professor',
        ),
    ]
