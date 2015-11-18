# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comunioapp', '0003_auto_20151105_0745'),
    ]

    operations = [
        migrations.RenameField(
            model_name='equipo',
            old_name='descripcion',
            new_name='estadio',
        ),
    ]
