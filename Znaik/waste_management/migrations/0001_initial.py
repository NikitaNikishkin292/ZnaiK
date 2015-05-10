# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bin_id', models.IntegerField(default=1)),
                ('bin_x_coord', models.DecimalField(max_digits=10, decimal_places=8)),
                ('bin_y_coord', models.DecimalField(max_digits=10, decimal_places=8)),
                ('bin_adress', models.CharField(max_length=200)),
                ('bin_volume', models.IntegerField(default=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Measurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('measurement_date', models.DateTimeField()),
                ('voulume_of_recycle_inside', models.IntegerField(default=0)),
                ('mass_of_recycle_inside', models.DecimalField(max_digits=3, decimal_places=1)),
                ('bin', models.ForeignKey(to='waste_management.Bin')),
            ],
        ),
    ]
