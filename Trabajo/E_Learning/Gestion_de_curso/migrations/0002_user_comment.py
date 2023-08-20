# Generated by Django 4.2.4 on 2023-08-20 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_de_curso', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=200)),
                ('identidad', models.CharField(max_length=20)),
                ('contraseña', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('nombre_user', models.CharField(max_length=200)),
                ('identidad_user', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=1000)),
            ],
        ),
    ]
