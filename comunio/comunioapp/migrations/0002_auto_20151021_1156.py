# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comunioapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('numero', models.CharField(max_length=30)),
                ('jugadores', models.TextField()),
                ('fecha', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='comunioapp',
        ),
    ]
