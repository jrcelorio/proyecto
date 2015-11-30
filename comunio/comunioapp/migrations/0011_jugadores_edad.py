# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comunioapp', '0010_remove_jugadores_edad'),
    ]

    operations = [
        migrations.AddField(
            model_name='jugadores',
            name='edad',
            field=models.IntegerField(null=True),
        ),
    ]
