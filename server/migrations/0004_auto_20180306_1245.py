# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0003_auto_20180306_1046'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='data',
            field=models.CharField(max_length=2048),
        ),
    ]
