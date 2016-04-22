import graphene
from graphene import relay, ObjectType
from graphene.contrib.django.filter import DjangoFilterConnectionField
from graphene.contrib.django.types import DjangoNode, DjangoConnection
from crunchbase.models import *

class Connection(DjangoConnection):
    total_count = graphene.Int()

    def resolve_total_count(self, args, info):
        return len(self.get_connection_data())

class FundingRoundNode(DjangoNode):
	class Meta:
		model = CbFundingRounds
		filter_fields = {'id'                   : {'exact'}, 
		                 'funding_round_id'     : {'exact'}, 
		                 'object'               : {'exact'}, 
		                 'funded_at'            : {'exact', 'lt', 'gt'},
		                 'funding_round_type'   : {'iexact'},
		                 'funding_round_code'   : {'iexact'},
		                 'raised_amount_usd'    : {'exact', 'lt', 'gt'},
		                 'raised_amount'        : {'exact', 'lt', 'gt'},
		                 'raised_currency_code' : {'iexact'},
		                 'participants'         : {'exact', 'lt', 'gt'},
		                 'is_first_round'       : {'exact'},
		                 'is_last_round'        : {'exact'},
		                 'source_url'           : {'iexact'},
		                 'source_description'   : {'iexact', 'icontains'},
		                 'created_by'           : {'iexact'},
		                 'created_at'           : {'exact', 'lt', 'gt'},
		                 'updated_at'           : {'exact', 'lt', 'gt'},
		                  }
	connection_type = Connection


class ObjectNode(DjangoNode):
	class Meta:
		model = CbObjects
		filter_fields = {'id': {},
		                 'entity_type'          : {'iexact'},
		                 'entity_id'            : {'exact'},
		                 'parent_id'            : {'exact'},
		                 'name'                 : {'iexact', 'istartswith'},
		                 'normalized_name'      : {'iexact', 'istartswith'},
		                 'permalink'            : {'iexact', 'istartswith', 'icontains'},
		                 'category_code'        : {'iexact'},
		                 'status'               : {'iexact'},
		                 'founded_at'           : {'exact', 'lt', 'gt'},
		                 'closed_at'            : {'exact', 'lt', 'gt'},
		                 'domain'               : {'iexact'},
		                 'homepage_url'         : {'iexact', 'icontains'},
		                 'twitter_username'     : {'iexact'},
		                 'logo_url'             : {'iexact'},
		                 'logo_width'           : {'exact', 'lt', 'gt'},
		                 'logo_height'          : {'exact', 'lt', 'gt'},
		                 'short_description'    : {'icontains'},
		                 'description'          : {'icontains'},
		                 'overview'             : {'icontains'},
		                 'tag_list'             : {'icontains'},
		                 'country_code'         : {'iexact'},
		                 'state_code'           : {'iexact'},
		                 'city'                 : {'iexact'},
		                 'region'               : {'iexact'},
		                 'first_investment_at'  : {'exact', 'lt', 'gt'},
		                 'last_investment_at'   : {'exact', 'lt', 'gt'},
		                 'investment_rounds'    : {'exact', 'lt', 'gt'},
		                 'invested_companies'   : {'exact', 'lt', 'gt'},
		                 'first_funding_at'     : {'exact', 'lt', 'gt'},
		                 'last_funding_at'      : {'exact', 'lt', 'gt'},
		                 'funding_rounds'       : {'exact', 'lt', 'gt'},
		                 'funding_total_usd'    : {'exact', 'lt', 'gt'},
		                 'first_milestone_at'   : {'exact', 'lt', 'gt'},
		                 'last_milestone_at'    : {'exact', 'lt', 'gt'},
		                 'milestones'           : {'exact', 'lt', 'gt'},
		                 'relationships'        : {'exact', 'lt', 'gt'},
		                 'created_by'           : {'exact'},
		                 'created_at'           : {'exact', 'lt', 'gt'},
		                 'updated_at'           : {'exact', 'lt', 'gt'},
		                 }
	connection_type = Connection


class RelationshipNode(DjangoNode):
	class Meta:
		model = CbRelationships
		filter_fields = {'id'                   : {'exact'},
		                 'relationship_id'      : {'exact'},
		                 'person_object'        : {'exact'},
		                 'relationship_object'  : {'exact'},
		                 'start_at'             : {'exact', 'lt', 'gt'},
		                 'end_at'               : {'exact', 'lt', 'gt'},
		                 'is_past'              : {'exact'},
		                 'sequence'             : {'exact'},
		                 'title'                : {'iexact'},
		                 'created_at'           : {'exact', 'lt', 'gt'},
		                 'updated_at'           : {'exact', 'lt', 'gt'},
		                 }
	connection_type = Connection


class DegreeNode(DjangoNode):
	class Meta:
		model = CbDegrees
		filter_fields = {'id'                   : {'exact'},
		                 'object'               : {'exact'},
		                 'institution'          : {'iexact', 'istartswith'},
						 'degree_type'          : {'iexact', 'istartswith'},
						 'subject'              : {'iexact', 'istartswith'},
						 'graduated_at'         : {'exact', 'lt', 'gt'},
						 'created_at'           : {'exact', 'lt', 'gt'},
						 'updated_at'           : {'exact', 'lt', 'gt'},
						 }
	connection_type = Connection


class AcquisitionNode(DjangoNode):
	class Meta:
		model = CbAcquisitions
		filter_fields = {'id'                   : {'exact'},
		                 'acquisition_id'       : {'exact'},
		                 'acquiring_object'     : {'exact'},
		                 'acquired_object'      : {'exact'},
		                 'term_code'            : {'exact'},
		                 'price_amount'         : {'exact', 'lt', 'gt'},
		                 'price_currency_code'  : {'exact'},
		                 'acquired_at'          : {'exact', 'lt', 'gt'},
		                 'source_url'           : {'exact'},
		                 'source_description'   : {'icontains'},
		                 'created_at'           : {'exact', 'lt', 'gt'},
		                 'updated_at'           : {'exact', 'lt', 'gt'},
		                 }
	connection_type = Connection


class FundNode(DjangoNode):
	class Meta:
		model = CbFunds
		filter_fields = {'id'                   : {'exact'},
		                 'fund_id'              : {'exact'},
		                 'object'               : {'exact'},
		                 'name'                 : {'iexact', 'istartswith'},
		                 'funded_at'            : {'exact', 'lt', 'gt'},
		                 'raised_amount'        : {'exact', 'lt', 'gt'},
		                 'raised_currency_code' : {'exact'},
		                 'source_url'           : {'exact'},
		                 'source_description'   : {'icontains'},
		                 'created_at'           : {'exact', 'lt', 'gt'},
		                 'updated_at'           : {'exact', 'lt', 'gt'},
		                 }
	connection_type = Connection


class InvestmentNode(DjangoNode):
	class Meta:
		model = CbInvestments
		filter_fields = {'id'                   : {'exact'}, 
		                 'funding_round'        : {'exact'},
		                 'funded_object'        : {'exact'},
		                 'investor_object'      : {'exact'},
		                 'created_at'           : {'exact', 'lt', 'gt'},
		                 'updated_at'           : {'exact', 'lt', 'gt'},
		                 }
	connection_type = Connection


class IpoNode(DjangoNode):
	class Meta:
		model = CbIpos
		filter_fields = {'id'                   : {'exact'},
		                 'ipo_id'               : {'exact'},
		                 'object'               : {'exact'},
		                 'valuation_amount'     : {'exact', 'lt', 'gt'},
		                 'valuation_currency_code': {'exact'},
		                 'raised_amount'        : {'exact', 'lt', 'gt'},
		                 'raised_currency_code' : {'exact'},
		                 'public_at'            : {'exact', 'lt', 'gt'},
		                 'stock_symbol'         : {'exact'},
		                 'source_url'           : {'exact'},
		                 'source_description'   : {'icontains'},
		                 'created_at'           : {'exact', 'lt', 'gt'},
		                 'updated_at'           : {'exact', 'lt', 'gt'},

		                 }
	connection_type = Connection


class MilestoneNode(DjangoNode):
	class Meta:
		model = CbMilestones
		filter_fields = {'id'                   : {'exact'},
		                 'object'               : {'exact'},
		                 'milestone_at'         : {'exact', 'lt', 'gt'},
		                 'milestone_code'       : {'exact'},
		                 'description'          : {'icontains'},
		                 'source_url'           : {'exact'},
		                 'source_description'   : {'icontains'},
		                 'created_at'           : {'exact', 'lt', 'gt'},
		                 'updated_at'           : {'exact', 'lt', 'gt'},
		                 }
	connection_type = Connection


class OfficeNode(DjangoNode):
	class Meta:
		model = CbOffices
		filter_fields = {'id'                   : {'exact'},
		                 'object'               : {'exact'},
		                 'office_id'            : {'exact'},
		                 'description'          : {'icontains'},
		                 'region'               : {'exact'},
		                 'address1'             : {'icontains'},
		                 'address2'             : {'icontains'},
		                 'city'                 : {'exact'},
		                 'zip_code'             : {'exact'},
		                 'state_code'           : {'exact'},
		                 'country_code'         : {'exact'},
		                 'latitude'             : {'exact', 'lt', 'gt'},
		                 'longitude'            : {'exact', 'lt', 'gt'},
		                 'created_at'           : {'exact', 'lt', 'gt'},
		                 'updated_at'           : {'exact', 'lt', 'gt'},
		                 }
	connection_type = Connection


class PeopleNode(DjangoNode):
	class Meta:
		model = CbPeople
		filter_fields = {'id'                   : {'exact'},
		                 'object'               : {'exact'},
		                 'first_name'           : {'iexact', 'istartswith'},
		                 'last_name'            : {'iexact', 'istartswith'},
		                 'birthplace'           : {'iexact'},
		                 'affiliation_name'     : {'iexact'},
		                 }
	connection_type = Connection

class Query(ObjectType):
	fundingRound = relay.NodeField(FundingRoundNode)
	allFundingRounds = DjangoFilterConnectionField(FundingRoundNode)

	object = relay.NodeField(ObjectNode)
	allObjects = DjangoFilterConnectionField(ObjectNode)

	relationship = relay.NodeField(RelationshipNode)
	allRelationships = DjangoFilterConnectionField(RelationshipNode)

	degree = relay.NodeField(DegreeNode)
	allDegrees = DjangoFilterConnectionField(DegreeNode)

	acquisition = relay.NodeField(AcquisitionNode)
	allAcquisitions = DjangoFilterConnectionField(AcquisitionNode)

	fund = relay.NodeField(FundNode)
	allFunds = DjangoFilterConnectionField(FundNode)

	investment = relay.NodeField(InvestmentNode)
	allInvestments = DjangoFilterConnectionField(InvestmentNode)

	ipo = relay.NodeField(IpoNode)
	allIpos = DjangoFilterConnectionField(IpoNode)

	milestone = relay.NodeField(MilestoneNode)
	allMilestones = DjangoFilterConnectionField(MilestoneNode)

	office = relay.NodeField(OfficeNode)
	allOffices = DjangoFilterConnectionField(OfficeNode)

	people = relay.NodeField(PeopleNode)
	allPeople = DjangoFilterConnectionField(PeopleNode)

	myObjects = relay.ConnectionField(ObjectNode, \
		description='Get objects by params.', \
		limit=graphene.Int(), \
		school=graphene.String(), \
		isInvestor=graphene.Boolean()
		)

	def resolve_myObjects(self, args, info):
		limit = args.get('limit')
		school = args.get('school')

		if (school is not None) and (school != ''): 
			ret = []
			len = 0
			degrees = CbDegrees.objects.filter(institution=school)
			for degree in degrees:
				if len == limit:
					break
				ret.append(degree.object)
				len += 1
			return ret
		return CbObjects.objects.all()[:limit]

	class Meta:
		abstract = True