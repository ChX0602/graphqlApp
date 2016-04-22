# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-04-16 01:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CbAcquisitions',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('acquisition_id', models.BigIntegerField()),
                ('acquiring_object_id', models.CharField(max_length=64)),
                ('acquired_object_id', models.CharField(max_length=64)),
                ('term_code', models.CharField(blank=True, max_length=16, null=True)),
                ('price_amount', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('price_currency_code', models.CharField(blank=True, max_length=16, null=True)),
                ('acquired_at', models.DateField(blank=True, null=True)),
                ('source_url', models.CharField(blank=True, max_length=255, null=True)),
                ('source_description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cb_acquisitions',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CbDegrees',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.CharField(max_length=64)),
                ('degree_type', models.CharField(max_length=32)),
                ('subject', models.CharField(blank=True, max_length=255, null=True)),
                ('institution', models.CharField(blank=True, max_length=64, null=True)),
                ('graduated_at', models.DateField(blank=True, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cb_degrees',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CbFundingRounds',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('funding_round_id', models.BigIntegerField()),
                ('object_id', models.CharField(max_length=64)),
                ('funded_at', models.DateField(blank=True, null=True)),
                ('funding_round_type', models.CharField(blank=True, max_length=32, null=True)),
                ('funding_round_code', models.CharField(blank=True, max_length=32, null=True)),
                ('raised_amount_usd', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('raised_amount', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('raised_currency_code', models.CharField(blank=True, max_length=3, null=True)),
                ('pre_money_valuation_usd', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('pre_money_valuation', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('pre_money_currency_code', models.CharField(blank=True, max_length=3, null=True)),
                ('post_money_valuation_usd', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('post_money_valuation', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('post_money_currency_code', models.CharField(blank=True, max_length=3, null=True)),
                ('participants', models.IntegerField(blank=True, null=True)),
                ('is_first_round', models.IntegerField(blank=True, null=True)),
                ('is_last_round', models.IntegerField(blank=True, null=True)),
                ('source_url', models.CharField(blank=True, max_length=255, null=True)),
                ('source_description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_by', models.CharField(blank=True, max_length=64, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cb_funding_rounds',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CbFunds',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fund_id', models.BigIntegerField()),
                ('object_id', models.CharField(max_length=64)),
                ('name', models.CharField(max_length=255)),
                ('funded_at', models.DateField(blank=True, null=True)),
                ('raised_amount', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('raised_currency_code', models.CharField(blank=True, max_length=3, null=True)),
                ('source_url', models.CharField(blank=True, max_length=255, null=True)),
                ('source_description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cb_funds',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CbInvestments',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('funding_round_id', models.BigIntegerField()),
                ('funded_object_id', models.CharField(max_length=64)),
                ('investor_object_id', models.CharField(max_length=64)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cb_investments',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CbIpos',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('ipo_id', models.BigIntegerField()),
                ('object_id', models.CharField(max_length=64)),
                ('valuation_amount', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('valuation_currency_code', models.CharField(blank=True, max_length=16, null=True)),
                ('raised_amount', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('raised_currency_code', models.CharField(blank=True, max_length=16, null=True)),
                ('public_at', models.DateField(blank=True, null=True)),
                ('stock_symbol', models.CharField(blank=True, max_length=32, null=True)),
                ('source_url', models.CharField(blank=True, max_length=255, null=True)),
                ('source_description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cb_ipos',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CbMilestones',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.CharField(max_length=64)),
                ('milestone_at', models.DateField(blank=True, null=True)),
                ('milestone_code', models.CharField(blank=True, max_length=32, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('source_url', models.CharField(blank=True, max_length=255, null=True)),
                ('source_description', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cb_milestones',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CbObjects',
            fields=[
                ('id', models.CharField(max_length=64, primary_key=True, serialize=False)),
                ('entity_type', models.CharField(max_length=16)),
                ('entity_id', models.BigIntegerField()),
                ('parent_id', models.CharField(blank=True, max_length=64, null=True)),
                ('name', models.CharField(max_length=255)),
                ('normalized_name', models.CharField(max_length=255)),
                ('permalink', models.CharField(max_length=255)),
                ('category_code', models.CharField(blank=True, max_length=32, null=True)),
                ('status', models.CharField(blank=True, max_length=32, null=True)),
                ('founded_at', models.DateField(blank=True, null=True)),
                ('closed_at', models.DateField(blank=True, null=True)),
                ('domain', models.CharField(blank=True, max_length=64, null=True)),
                ('homepage_url', models.CharField(blank=True, max_length=64, null=True)),
                ('twitter_username', models.CharField(blank=True, max_length=64, null=True)),
                ('logo_url', models.CharField(blank=True, max_length=255, null=True)),
                ('logo_width', models.IntegerField(blank=True, null=True)),
                ('logo_height', models.IntegerField(blank=True, null=True)),
                ('short_description', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('overview', models.TextField(blank=True, null=True)),
                ('tag_list', models.CharField(blank=True, max_length=255, null=True)),
                ('country_code', models.CharField(blank=True, max_length=64, null=True)),
                ('state_code', models.CharField(blank=True, max_length=64, null=True)),
                ('city', models.CharField(blank=True, max_length=64, null=True)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('first_investment_at', models.DateField(blank=True, null=True)),
                ('last_investment_at', models.DateField(blank=True, null=True)),
                ('investment_rounds', models.IntegerField(blank=True, null=True)),
                ('invested_companies', models.IntegerField(blank=True, null=True)),
                ('first_funding_at', models.DateField(blank=True, null=True)),
                ('last_funding_at', models.DateField(blank=True, null=True)),
                ('funding_rounds', models.IntegerField(blank=True, null=True)),
                ('funding_total_usd', models.DecimalField(blank=True, decimal_places=0, max_digits=15, null=True)),
                ('first_milestone_at', models.DateField(blank=True, null=True)),
                ('last_milestone_at', models.DateField(blank=True, null=True)),
                ('milestones', models.IntegerField(blank=True, null=True)),
                ('relationships', models.IntegerField(blank=True, null=True)),
                ('created_by', models.CharField(blank=True, max_length=64, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cb_objects',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CbOffices',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.CharField(max_length=64)),
                ('office_id', models.BigIntegerField()),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('region', models.CharField(blank=True, max_length=255, null=True)),
                ('address1', models.CharField(blank=True, max_length=255, null=True)),
                ('address2', models.CharField(blank=True, max_length=255, null=True)),
                ('city', models.CharField(blank=True, max_length=255, null=True)),
                ('zip_code', models.CharField(blank=True, max_length=255, null=True)),
                ('state_code', models.CharField(blank=True, max_length=3, null=True)),
                ('country_code', models.CharField(blank=True, max_length=3, null=True)),
                ('latitude', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=10, max_digits=15, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cb_offices',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CbPeople',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('object_id', models.CharField(max_length=64, unique=True)),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('birthplace', models.CharField(blank=True, max_length=128, null=True)),
                ('affiliation_name', models.CharField(blank=True, max_length=128, null=True)),
            ],
            options={
                'db_table': 'cb_people',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='CbRelationships',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('relationship_id', models.BigIntegerField()),
                ('person_object_id', models.CharField(max_length=64)),
                ('relationship_object_id', models.CharField(max_length=64)),
                ('start_at', models.DateField(blank=True, null=True)),
                ('end_at', models.DateField(blank=True, null=True)),
                ('is_past', models.IntegerField(blank=True, null=True)),
                ('sequence', models.IntegerField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'cb_relationships',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='cbobjects',
            unique_together=set([('entity_type', 'entity_id')]),
        ),
    ]