# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-12 06:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0007_auto_20161010_2252'),
    ]

    operations = [
        migrations.AddField(
            model_name='artista',
            name='val_imagen',
            field=models.CharField(blank=True, help_text='URL de la imagen del artista', max_length=1000, verbose_name='Imágen'),
        ),
    ]