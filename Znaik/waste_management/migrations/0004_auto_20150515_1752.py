# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('waste_management', '0003_auto_20150510_1441'),
    ]

    operations = [
        migrations.RenameField(
            model_name='measurement',
            old_name='voulume_of_recycle_inside',
            new_name='volume_of_recycle_inside',
        ),
    ]
