# Generated by Django 2.1.1 on 2018-12-03 22:34

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0004_estudiante'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='Aprobados',
            field=django.contrib.postgres.fields.jsonb.JSONField(),
        ),
    ]