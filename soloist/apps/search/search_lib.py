from elasticsearch_dsl import FacetedSearch, TermsFacet
from django.conf import settings


class WorklogSearch(FacetedSearch):

    index = [settings.ES_INDEX, ]

    # "tables" that should be searched
    doc_types = ['worklog', ]

    # fields that should be searched
    fields = ['pwa_note', ]

    facets = {
        'portals': TermsFacet(field='pa_code'),
        'clients': TermsFacet(field='pca_code'),
        'categories': TermsFacet(field='facet_category'),
    }

    def query(self, search, query):
        """Overwrites query type to `phrase`"""
        if query:
            return search.query('multi_match', fields=self.fields, query=query, type='phrase')
        return search
