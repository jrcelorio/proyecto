# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comunioapp', '0007_noticias'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo_jugador',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('jornada', models.IntegerField()),
                ('equipo', models.ForeignKey(to='comunioapp.Equipo')),
            ],
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('numero', models.TextField()),
                ('puntuacion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='jugador_jornada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('puntuación', models.IntegerField()),
                ('jornada', models.ForeignKey(to='comunioapp.Jornada')),
            ],
        ),
        migrations.RenameField(
            model_name='noticias',
            old_name='noticias',
            new_name='descripcion',
        ),
        migrations.AddField(
            model_name='jugadores',
            name='edad',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='jugadores',
            name='equipo',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='jugadores',
            name='equipos',
            field=models.ManyToManyField(through='comunioapp.Equipo_jugador', to='comunioapp.Equipo'),
        ),
        migrations.AddField(
            model_name='jugador_jornada',
            name='jugadores',
            field=models.ForeignKey(to='comunioapp.Jugadores'),
        ),
        migrations.AddField(
            model_name='equipo_jugador',
            name='jugadores',
            field=models.ForeignKey(to='comunioapp.Jugadores'),
        ),
    ]
