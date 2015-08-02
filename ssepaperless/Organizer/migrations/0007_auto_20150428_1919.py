# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0006_auto_20150428_1917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='StudyPlan',
            field=models.CharField(default=b'Y', max_length=2, choices=[(b'Y', b'Yes'), (b'N', b'No'), (b'IP', b'In Progress')]),
            preserve_default=True,
        ),
    ]
