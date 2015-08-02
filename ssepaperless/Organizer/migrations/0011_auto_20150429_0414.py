# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0010_auto_20150428_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='CertificateRequiredCourse',
            field=models.ManyToManyField(to='Organizer.Certificate', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='student',
            name='StudyPlanPDF',
            field=models.FileField(upload_to=b'StudyPlanPDF/', blank=True),
            preserve_default=True,
        ),
    ]
