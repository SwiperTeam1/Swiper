# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-12-23 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Swiped',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.IntegerField(verbose_name='用户自身id')),
                ('sid', models.IntegerField(verbose_name='被滑的陌生人id')),
                ('mark', models.CharField(choices=[('like', 'like'), ('dislike', 'dislike'), ('superlike', 'superlike')], max_length=16, verbose_name='滑动类型')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='滑动的时间')),
            ],
        ),
    ]
