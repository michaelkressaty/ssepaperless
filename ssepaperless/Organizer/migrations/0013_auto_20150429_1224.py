# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Organizer', '0012_remove_certificate_advisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='CertificateName',
            field=models.CharField(max_length=200),
            preserve_default=True,
        ),
    ]
