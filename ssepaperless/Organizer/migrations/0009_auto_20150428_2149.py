# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0008_remove_degree_core_course_structure_requiredcore'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate_course_structure',
            name='Required_Course',
        ),
        migrations.RemoveField(
            model_name='degree_elective_course_structure',
            name='ElectiveOption',
        ),
        migrations.AddField(
            model_name='course',
            name='CertificateRequiredCourse',
            field=models.ManyToManyField(to='Organizer.Certificate_Course_Structure'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='ElectiveOption',
            field=models.ManyToManyField(to='Organizer.Degree_Elective_Course_Structure'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='course',
            name='RequiredCore',
            field=models.ManyToManyField(to='Organizer.Degree_Core_Course_Structure'),
            preserve_default=True,
        ),
    ]
