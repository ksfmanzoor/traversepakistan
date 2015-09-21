# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_remove_place_gallerypath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='coverImage',
            field=models.CharField(max_length=256),
        ),
    ]
