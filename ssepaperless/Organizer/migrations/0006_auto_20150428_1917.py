# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0005_student_semesteraccepted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='StudyPlan',
            field=models.CharField(default=b'Y', max_length=2, choices=[(b'Yes', b'Yes'), (b'No', b'No'), (b'In Progress', b'In Progress')]),
            preserve_default=True,
        ),
    ]
