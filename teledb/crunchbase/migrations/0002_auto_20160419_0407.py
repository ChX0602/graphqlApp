# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-19 04:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crunchbase', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cbacquisitions',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cbdegrees',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cbfundingrounds',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cbfunds',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cbinvestments',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cbipos',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cbmilestones',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cbobjects',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cboffices',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cbpeople',
            options={},
        ),
        migrations.AlterModelOptions(
            name='cbrelationships',
            options={},
        ),
        migrations.AddField(
            model_name='cbobjects',
            name='employments',
            field=models.ManyToManyField(through='crunchbase.CbRelationships', to='crunchbase.CbObjects'),
        ),
        migrations.AlterField(
            model_name='cbfundingrounds',
            name='object_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='CbFundingRounds', to='crunchbase.CbObjects'),
        ),
        migrations.AlterField(
            model_name='cbrelationships',
            name='person_object_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employees', to='crunchbase.CbObjects'),
        ),
        migrations.AlterField(
            model_name='cbrelationships',
            name='relationship_object_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='employers', to='crunchbase.CbObjects'),
        ),
    ]