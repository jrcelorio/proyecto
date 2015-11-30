# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comunioapp', '0004_auto_20151109_0815'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equipo_jugador',
            name='equipo',
        ),
        migrations.RemoveField(
            model_name='equipo_jugador',
            name='jugadores',
        ),
        migrations.RemoveField(
            model_name='jugador_jornada',
            name='jornada',
        ),
        migrations.RemoveField(
            model_name='jugador_jornada',
            name='jugadores',
        ),
        migrations.DeleteModel(
            name='Noticias',
        ),
        migrations.RenameField(
            model_name='equipo',
            old_name='estadio',
            new_name='descripcion',
        ),
        migrations.RemoveField(
            model_name='jugadores',
            name='edad',
        ),
        migrations.RemoveField(
            model_name='jugadores',
            name='equipo',
        ),
        migrations.RemoveField(
            model_name='jugadores',
            name='equipos',
        ),
        migrations.DeleteModel(
            name='Equipo_jugador',
        ),
        migrations.DeleteModel(
            name='Jornada',
        ),
        migrations.DeleteModel(
            name='jugador_jornada',
        ),
    ]
