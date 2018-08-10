# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-06-20 12:57
from __future__ import unicode_literals

from django.db import migrations, models
import uuid


def set_dashboard_uuid(apps, schema_editor):
    Dashboard = apps.get_model('workflow', 'Dashboard')
    for dashboard in Dashboard.objects.all():
        dashboard.dashboard_uuid = uuid.uuid4()
        dashboard.save()


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0024_auto_20180620_0537'),
    ]

    operations = [
        migrations.RunPython(set_dashboard_uuid),
        migrations.AlterField(
            model_name='dashboard',
            name='dashboard_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Dashboard UUID'),
        ),
    ]