# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 08:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('workflow', '0001_initial'),
        ('customdashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jupyternotebooks',
            name='workflowlevel1',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workflow.WorkflowLevel1'),
        ),
    ]
