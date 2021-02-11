# Generated by Django 3.1.6 on 2021-02-09 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellidos', models.CharField(max_length=100)),
                ('nombre', models.CharField(blank=True, max_length=100)),
                ('fecha_nacimiento', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('anio', models.CharField(max_length=10)),
                ('editorial', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True)),
                ('genero', models.IntegerField(blank=True, choices=[(1, 'NOVELA'), (2, 'ENSAYOS')])),
                ('autor', models.ManyToManyField(blank=True, to='libros.Autor')),
            ],
        ),
    ]
