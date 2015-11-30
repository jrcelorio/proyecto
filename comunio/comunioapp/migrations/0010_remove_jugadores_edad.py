# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comunioapp', '0009_remove_jugadores_equipo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jugadores',
            name='edad',
        ),
    ]
