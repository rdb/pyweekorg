# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-07 18:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_usersettings_email_replies'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='emailaddress',
            options={'verbose_name_plural': 'email addresses'},
        ),
        migrations.AlterModelOptions(
            name='usersettings',
            options={'verbose_name_plural': 'user settings'},
        ),
    ]
