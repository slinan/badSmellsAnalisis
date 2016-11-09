# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-29 04:06
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenido', '0010_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('val_rating', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('fec_creacion_rating', models.DateTimeField(auto_now_add=True, help_text='Fecha de creación del rating')),
                ('audio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenido.Audio')),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]