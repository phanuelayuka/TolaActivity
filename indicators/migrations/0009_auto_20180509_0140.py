# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-05-09 08:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indicators', '0008_disaggregationvalue_indicator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disaggregationlabel',
            name='disaggregation_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='indicators.DisaggregationType'),
        ),
        migrations.AlterField(
            model_name='disaggregationvalue',
            name='disaggregation_label',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='indicators.DisaggregationLabel'),
        ),
    ]
