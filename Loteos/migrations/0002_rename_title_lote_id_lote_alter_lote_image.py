# Generated by Django 4.1.6 on 2023-09-04 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Loteos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lote',
            old_name='title',
            new_name='id_lote',
        ),
        migrations.AlterField(
            model_name='lote',
            name='image',
            field=models.ImageField(default='Null', upload_to='obras', verbose_name='Imagen'),
        ),
    ]
