# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_place_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='galleryPath',
        ),
    ]
