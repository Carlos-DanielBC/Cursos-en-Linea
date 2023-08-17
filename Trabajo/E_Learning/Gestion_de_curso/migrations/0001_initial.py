# Generated by Django 3.2.20 on 2023-08-15 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('descripcion', models.TextField()),
                ('nivel_dificultad', models.CharField(max_length=20)),
                ('materiales_educativos', models.FileField(upload_to='materiales/')),
            ],
        ),
    ]
    

