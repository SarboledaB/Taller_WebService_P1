# Generated by Django 3.0.6 on 2020-05-13 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('luminosity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='luminosity',
            name='latitud',
            field=models.DecimalField(decimal_places=5, default=0, max_digits=6, verbose_name='lat'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='luminosity',
            name='longitud',
            field=models.DecimalField(decimal_places=5, default=1, max_digits=6, verbose_name='lng'),
            preserve_default=False,
        ),
    ]
