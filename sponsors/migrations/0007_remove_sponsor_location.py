# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sponsors', '0006_auto_20150914_1300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sponsor',
            name='location',
        ),
    ]
