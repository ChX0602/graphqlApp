import sys
from crunchbase.models import *

def get_grow_time():
	time = 0
	count = 0;
	err_count = 0;
	funding_rounds = CbFundingRounds.objects.filter(funding_round_type='series-b')
	for funding_round in funding_rounds:
		try:
			object_id = funding_round.object_id

			obj = CbObjects.objects.get(id=object_id, entity_type='Company')
			

			first_date = CbFundingRounds.objects.filter(object_id=object_id, funding_round_type='series-a').order_by('funded_at')[0].funded_at

			second_date = CbFundingRounds.objects.filter(object_id=object_id, funding_round_type='series-b').order_by('funded_at').reverse()[0].funded_at
			duration = (second_date - first_date).days

			time += duration
			count += 1
		except:
			#print "Unexpected error:", sys.exc_info()[0]
			err_count += 1
	return time / count
