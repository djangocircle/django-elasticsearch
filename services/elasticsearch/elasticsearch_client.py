import uuid

from elasticsearch import Elasticsearch
from elasticsearch_dsl import connections
from django.conf import settings


es_client = Elasticsearch()

try:
    connections.create_connection(
        timeout=15,
        hosts=settings.ELASTIC_CLOUD_HOSTS,
        http_auth=(
            settings.ELASTIC_CLOUD_USER,
            settings.ELASTIC_CLOUD_PASSWORD,
        ),
    )
except (TypeError, OSError):
    pass    


def create_document(index_name, body={}):
    print(body)
    return es_client.create(
            index=index_name,  
            id=uuid.uuid4(), 
            body=body
        )


