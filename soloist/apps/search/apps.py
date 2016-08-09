from django.apps import AppConfig
from django.conf import settings
from elasticsearch_dsl.connections import connections


class SearchConfig(AppConfig):
    name = 'soloist.apps.search'

    def ready(self):
        connections.configure(**settings.ES_CONNECTIONS)
