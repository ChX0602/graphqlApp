import graphene

from crunchbase import schema

class Query(schema.Query):
	pass
	
schema = graphene.Schema(name='Crunchbase Schema')
schema.query = Query