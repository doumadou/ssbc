# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_auto_20150511_0339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hash',
            name='files_count',
            field=models.IntegerField(default=1),
        ),
    ]
