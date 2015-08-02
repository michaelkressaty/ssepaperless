# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0007_auto_20150428_1919'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='degree_core_course_structure',
            name='RequiredCore',
        ),
    ]
