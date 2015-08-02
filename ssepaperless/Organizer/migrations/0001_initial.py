# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('AdvisorName', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CertificateName', models.CharField(max_length=75)),
                ('Department', models.ManyToManyField(to='Organizer.Advisor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Certificate_Course_Structure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Certificate_Course_Structure_ID', models.CharField(max_length=50)),
                ('Certificate', models.ForeignKey(to='Organizer.Certificate')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CourseName', models.CharField(max_length=200)),
                ('CourseID', models.CharField(max_length=10)),
                ('Credits', models.IntegerField(max_length=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Degree',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DegreeName', models.CharField(max_length=75)),
                ('Advisors', models.ManyToManyField(to='Organizer.Advisor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Degree_Core_Course_Structure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Degree_Core_Course_Structure_ID', models.CharField(max_length=50)),
                ('Degree', models.ForeignKey(to='Organizer.Degree')),
                ('RequiredCore', models.ManyToManyField(to='Organizer.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Degree_Elective_Course_Structure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Degree_Elective_Course_Structure_ID', models.CharField(max_length=50)),
                ('Choose', models.IntegerField(max_length=2)),
                ('CoreRelation', models.OneToOneField(to='Organizer.Degree_Core_Course_Structure')),
                ('ElectiveOption', models.ManyToManyField(to='Organizer.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('DepartmentName', models.CharField(max_length=75)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('StudentName', models.CharField(max_length=75)),
                ('StudentID', models.IntegerField(max_length=8)),
                ('StudyPlanPDF', models.FileField(upload_to=b'StudyPlanPDF/')),
                ('Advisor', models.ForeignKey(to='Organizer.Advisor')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='certificate_course_structure',
            name='Required_Course',
            field=models.ManyToManyField(to='Organizer.Course'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='advisor',
            name='Department',
            field=models.ForeignKey(to='Organizer.Department'),
            preserve_default=True,
        ),
    ]
