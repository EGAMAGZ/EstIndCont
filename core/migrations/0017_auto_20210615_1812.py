# Generated by Django 3.1.2 on 2021-06-15 23:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_delete_marketrate'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='prosoftdoc',
            options={'ordering': ['created'], 'verbose_name': 'Documento de Prosoft', 'verbose_name_plural': 'Documentos de Prosoft'},
        ),
    ]
