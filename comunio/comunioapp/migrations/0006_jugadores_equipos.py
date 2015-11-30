# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comunioapp', '0005_auto_20151119_0853'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugadores',
            name='equipos',
            field=models.ManyToManyField(to='comunioapp.Equipo'),
        ),
    ]
