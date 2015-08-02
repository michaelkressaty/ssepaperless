# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0004_auto_20150428_1759'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='SemesterAccepted',
            field=models.CharField(default=b'S2105', max_length=5),
            preserve_default=True,
        ),
    ]
