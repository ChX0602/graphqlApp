import graphene

from crunchbase import schema

class query(crunchbase.schema.Query):
	pass
schema = graphene.schema(name='Crunchbase Schema')
schema.query = Query