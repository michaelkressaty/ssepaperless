# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0009_auto_20150428_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='CertificateRequiredCourse',
            field=models.ManyToManyField(to='Organizer.Certificate_Course_Structure', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='ElectiveOption',
            field=models.ManyToManyField(to='Organizer.Degree_Elective_Course_Structure', blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='course',
            name='RequiredCore',
            field=models.ManyToManyField(to='Organizer.Degree_Core_Course_Structure', blank=True),
            preserve_default=True,
        ),
    ]
