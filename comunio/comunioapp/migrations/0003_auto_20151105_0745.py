# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comunioapp', '0002_auto_20151021_1156'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipo_jugador',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('jornada', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jornada',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('numero', models.TextField()),
                ('puntuacion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='jugador_jornada',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('puntuación', models.IntegerField()),
                ('jornada', models.ForeignKey(to='comunioapp.Jornada')),
            ],
        ),
        migrations.CreateModel(
            name='Jugadores',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nombre', models.CharField(max_length=30)),
                ('equipo', models.TextField()),
                ('edad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Noticias',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='equipo',
            old_name='jugadores',
            new_name='descripcion',
        ),
        migrations.RenameField(
            model_name='equipo',
            old_name='numero',
            new_name='nombre',
        ),
        migrations.RemoveField(
            model_name='equipo',
            name='fecha',
        ),
        migrations.AddField(
            model_name='jugadores',
            name='equipos',
            field=models.ManyToManyField(to='comunioapp.Equipo', through='comunioapp.Equipo_jugador'),
        ),
        migrations.AddField(
            model_name='jugador_jornada',
            name='jugadores',
            field=models.ForeignKey(to='comunioapp.Jugadores'),
        ),
        migrations.AddField(
            model_name='equipo_jugador',
            name='equipo',
            field=models.ForeignKey(to='comunioapp.Equipo'),
        ),
        migrations.AddField(
            model_name='equipo_jugador',
            name='jugadores',
            field=models.ForeignKey(to='comunioapp.Jugadores'),
        ),
    ]
