# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0003_auto_20150428_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='Advisor',
            field=models.ManyToManyField(to='Organizer.Advisor'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='degree',
            name='Department',
            field=models.ManyToManyField(to='Organizer.Department'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='certificate',
            name='Department',
            field=models.ManyToManyField(to='Organizer.Department'),
            preserve_default=True,
        ),
    ]
