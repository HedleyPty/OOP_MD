# Generated by Django 2.1.4 on 2018-12-16 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0005_auto_20181203_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido',
            name='imagen',
            field=models.ImageField(blank=True, default='', upload_to=''),
        ),
    ]
