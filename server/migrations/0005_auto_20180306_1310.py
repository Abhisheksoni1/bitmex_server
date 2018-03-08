# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0004_auto_20180306_1245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='data',
            field=models.CharField(max_length=9632),
        ),
    ]
