# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waste_management', '0002_auto_20150510_1432'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bin',
            name='bin_x_coord',
        ),
        migrations.RemoveField(
            model_name='bin',
            name='bin_y_coord',
        ),
    ]
