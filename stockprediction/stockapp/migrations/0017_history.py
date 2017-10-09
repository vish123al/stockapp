# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-23 04:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0016_delete_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symbol', models.CharField(max_length=6)),
                ('date', models.DateField()),
                ('Open', models.DecimalField(decimal_places=10, max_digits=20)),
                ('high', models.DecimalField(decimal_places=10, max_digits=20)),
                ('low', models.DecimalField(decimal_places=10, max_digits=20)),
                ('close', models.DecimalField(decimal_places=10, max_digits=20)),
                ('volume', models.IntegerField()),
                ('adj_close', models.DecimalField(decimal_places=10, max_digits=20)),
            ],
        ),
    ]