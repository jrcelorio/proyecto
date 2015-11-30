# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comunioapp', '0008_auto_20151126_0845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jugadores',
            name='equipo',
        ),
    ]
