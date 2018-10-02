# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-02 21:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draftemail',
            name='sent',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='draftemail',
            name='status',
            field=models.IntegerField(choices=[(1, 'Draft'), (2, 'Sending'), (3, 'Sent')], default=1, editable=False),
        ),
    ]
