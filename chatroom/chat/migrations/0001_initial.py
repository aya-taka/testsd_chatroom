# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import swampdragon.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('authid', models.IntegerField()),
                ('text', models.TextField()),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('authid', models.IntegerField()),
                ('name', models.CharField(max_length=100)),
                ('des', models.TextField()),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.CreateModel(
            name='RoomResist',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('user', models.IntegerField()),
                ('room', models.IntegerField()),
            ],
            bases=(swampdragon.models.SelfPublishModel, models.Model),
        ),
        migrations.AddField(
            model_name='comment',
            name='room',
            field=models.ForeignKey(related_name='comment', to='chat.Room'),
        ),
    ]
