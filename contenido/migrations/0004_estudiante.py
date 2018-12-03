# Generated by Django 2.1.1 on 2018-12-03 22:32

from django.conf import settings
import django.contrib.auth.models
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
        ('contenido', '0003_auto_20181203_1046'),
    ]

    operations = [
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('Aprobados', django.contrib.postgres.fields.jsonb.JSONField(default={})),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]