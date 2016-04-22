# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class CbObjects(models.Model):
    id = models.CharField(primary_key=True, max_length=64)
    entity_type = models.CharField(max_length=16)
    entity_id = models.BigIntegerField()
    parent_id = models.CharField(max_length=64, blank=True, null=True)
    name = models.CharField(max_length=255)
    normalized_name = models.CharField(max_length=255)
    permalink = models.CharField(max_length=255)
    category_code = models.CharField(max_length=32, blank=True, null=True)
    status = models.CharField(max_length=32, blank=True, null=True)
    founded_at = models.DateField(blank=True, null=True)
    closed_at = models.DateField(blank=True, null=True)
    domain = models.CharField(max_length=64, blank=True, null=True)
    homepage_url = models.CharField(max_length=64, blank=True, null=True)
    twitter_username = models.CharField(max_length=64, blank=True, null=True)
    logo_url = models.CharField(max_length=255, blank=True, null=True)
    logo_width = models.IntegerField(blank=True, null=True)
    logo_height = models.IntegerField(blank=True, null=True)
    short_description = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    overview = models.TextField(blank=True, null=True)
    tag_list = models.CharField(max_length=255, blank=True, null=True)
    country_code = models.CharField(max_length=64, blank=True, null=True)
    state_code = models.CharField(max_length=64, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    first_investment_at = models.DateField(blank=True, null=True)
    last_investment_at = models.DateField(blank=True, null=True)
    investment_rounds = models.IntegerField(blank=True, null=True)
    invested_companies = models.IntegerField(blank=True, null=True)
    first_funding_at = models.DateField(blank=True, null=True)
    last_funding_at = models.DateField(blank=True, null=True)
    funding_rounds = models.IntegerField(blank=True, null=True)
    funding_total_usd = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    first_milestone_at = models.DateField(blank=True, null=True)
    last_milestone_at = models.DateField(blank=True, null=True)
    milestones = models.IntegerField(blank=True, null=True)
    relationships = models.IntegerField(blank=True, null=True)
    created_by = models.CharField(max_length=64, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    employments = models.ManyToManyField('self', through='CbRelationships', symmetrical=False)
    class Meta:
        db_table = 'cb_objects'
        unique_together = (('entity_type', 'entity_id'),)


class CbAcquisitions(models.Model):
    id = models.BigIntegerField(primary_key=True)
    acquisition_id = models.BigIntegerField()
    #acquiring_object_id = models.CharField(max_length=64)
    #acquired_object_id = models.CharField(max_length=64)
    acquiring_object = models.ForeignKey(CbObjects, related_name='RNacquiring')
    acquired_object = models.ForeignKey(CbObjects, related_name='RNacquired')
    term_code = models.CharField(max_length=16, blank=True, null=True)
    price_amount = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    price_currency_code = models.CharField(max_length=16, blank=True, null=True)
    acquired_at = models.DateField(blank=True, null=True)
    source_url = models.CharField(max_length=255, blank=True, null=True)
    source_description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'cb_acquisitions'


class CbFunds(models.Model):
    id = models.BigIntegerField(primary_key=True)
    fund_id = models.BigIntegerField()
    #object_id = models.CharField(max_length=64)
    object = models.ForeignKey(CbObjects)
    name = models.CharField(max_length=255)
    funded_at = models.DateField(blank=True, null=True)
    raised_amount = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    raised_currency_code = models.CharField(max_length=3, blank=True, null=True)
    source_url = models.CharField(max_length=255, blank=True, null=True)
    source_description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'cb_funds'


class CbFundingRounds(models.Model):
    id = models.BigIntegerField(primary_key=True)
    funding_round_id = models.BigIntegerField()
    #object_id = models.CharField(max_length=64)
    object = models.ForeignKey(CbObjects, related_name='RNfundingRounds')
    funded_at = models.DateField(blank=True, null=True)
    funding_round_type = models.CharField(max_length=32, blank=True, null=True)
    funding_round_code = models.CharField(max_length=32, blank=True, null=True)
    raised_amount_usd = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    raised_amount = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    raised_currency_code = models.CharField(max_length=3, blank=True, null=True)
    pre_money_valuation_usd = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    pre_money_valuation = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    pre_money_currency_code = models.CharField(max_length=3, blank=True, null=True)
    post_money_valuation_usd = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    post_money_valuation = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    post_money_currency_code = models.CharField(max_length=3, blank=True, null=True)
    participants = models.IntegerField(blank=True, null=True)
    is_first_round = models.IntegerField(blank=True, null=True)
    is_last_round = models.IntegerField(blank=True, null=True)
    source_url = models.CharField(max_length=255, blank=True, null=True)
    source_description = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.CharField(max_length=64, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'cb_funding_rounds'


class CbInvestments(models.Model):
    id = models.BigIntegerField(primary_key=True)
    #funding_round_id = models.BigIntegerField()
    #funded_object_id = models.CharField(max_length=64)
    #investor_object_id = models.CharField(max_length=64)
    funding_round = models.ForeignKey(CbFundingRounds, related_name='RNinvestments')
    funded_object = models.ForeignKey(CbObjects, related_name='RNfunded')
    investor_object = models.ForeignKey(CbObjects, related_name='RNinvesting')
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'cb_investments'


class CbIpos(models.Model):
    id = models.BigIntegerField(primary_key=True)
    ipo_id = models.BigIntegerField()
    #object_id = models.CharField(max_length=64)
    object = models.ForeignKey(CbObjects)
    valuation_amount = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    valuation_currency_code = models.CharField(max_length=16, blank=True, null=True)
    raised_amount = models.DecimalField(max_digits=15, decimal_places=0, blank=True, null=True)
    raised_currency_code = models.CharField(max_length=16, blank=True, null=True)
    public_at = models.DateField(blank=True, null=True)
    stock_symbol = models.CharField(max_length=32, blank=True, null=True)
    source_url = models.CharField(max_length=255, blank=True, null=True)
    source_description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'cb_ipos'


class CbMilestones(models.Model):
    id = models.BigIntegerField(primary_key=True)
    #object_id = models.CharField(max_length=64)
    object = models.ForeignKey(CbObjects)
    milestone_at = models.DateField(blank=True, null=True)
    milestone_code = models.CharField(max_length=32, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    source_url = models.CharField(max_length=255, blank=True, null=True)
    source_description = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'cb_milestones'


class CbDegrees(models.Model):
    id = models.BigIntegerField(primary_key=True)
    #object_id = models.CharField(max_length=64)
    object = models.ForeignKey(CbObjects, related_name='RNeducation')
    degree_type = models.CharField(max_length=32)
    subject = models.CharField(max_length=255, blank=True, null=True)
    institution = models.CharField(max_length=64, blank=True, null=True)
    graduated_at = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'cb_degrees'


class CbOffices(models.Model):
    id = models.BigIntegerField(primary_key=True)
    #object_id = models.CharField(max_length=64)
    object = models.ForeignKey(CbObjects)
    office_id = models.BigIntegerField()
    description = models.CharField(max_length=255, blank=True, null=True)
    region = models.CharField(max_length=255, blank=True, null=True)
    address1 = models.CharField(max_length=255, blank=True, null=True)
    address2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    zip_code = models.CharField(max_length=255, blank=True, null=True)
    state_code = models.CharField(max_length=3, blank=True, null=True)
    country_code = models.CharField(max_length=3, blank=True, null=True)
    latitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    longitude = models.DecimalField(max_digits=15, decimal_places=10, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'cb_offices'


class CbPeople(models.Model):
    id = models.BigIntegerField(primary_key=True)
    #object_id = models.CharField(unique=True, max_length=64)
    object = models.ForeignKey(CbObjects)
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    birthplace = models.CharField(max_length=128, blank=True, null=True)
    affiliation_name = models.CharField(max_length=128, blank=True, null=True)

    class Meta:
        db_table = 'cb_people'


class CbRelationships(models.Model):
    id = models.BigIntegerField(primary_key=True)
    relationship_id = models.BigIntegerField()
    #person_object_id = models.CharField(max_length=64)
    #relationship_object_id = models.CharField(max_length=64)
    person_object = models.ForeignKey(CbObjects, related_name='RNemployers')
    relationship_object = models.ForeignKey(CbObjects, related_name='RNemployees')
    start_at = models.DateField(blank=True, null=True)
    end_at = models.DateField(blank=True, null=True)
    is_past = models.IntegerField(blank=True, null=True)
    sequence = models.IntegerField(blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 'cb_relationships'