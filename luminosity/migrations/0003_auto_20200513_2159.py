# Generated by Django 3.0.6 on 2020-05-13 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminosity', '0002_auto_20200513_2125'),
    ]

    operations = [
        migrations.RenameField(
            model_name='luminosity',
            old_name='type',
            new_name='tipo',
        ),
        migrations.AlterField(
            model_name='luminosity',
            name='latitud',
            field=models.DecimalField(decimal_places=12, max_digits=12, verbose_name='latitud'),
        ),
        migrations.AlterField(
            model_name='luminosity',
            name='longitud',
            field=models.DecimalField(decimal_places=12, max_digits=12, verbose_name='longitud'),
        ),
    ]