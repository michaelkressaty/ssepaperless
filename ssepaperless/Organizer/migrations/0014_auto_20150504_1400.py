# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0013_auto_20150429_1224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='StudyPlan',
            new_name='StudyPlanApproved',
        ),
    ]
