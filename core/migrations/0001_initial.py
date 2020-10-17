# Generated by Django 3.1.2 on 2020-10-17 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_number', models.IntegerField(max_length=10, unique=True, verbose_name='Boleta')),
                ('profile_img', models.ImageField(upload_to='profile-img', verbose_name='Foto de Perfil')),
                ('name', models.CharField(max_length=60, verbose_name='Nombre')),
                ('surname', models.CharField(max_length=60, verbose_name='Apellido')),
                ('role', models.CharField(max_length=30, verbose_name='Cargo')),
            ],
        ),
    ]
