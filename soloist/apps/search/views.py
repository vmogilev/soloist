import logging
import pprint
from django.shortcuts import get_object_or_404, render
# from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# from elasticsearch_dsl import Search
# from elasticsearch_dsl.query import Match
from .search_lib import WorklogSearch


logger = logging.getLogger('django')


def serp(request):
    # index = settings.ES_INDEX
    # q = Match(pwa_note={"query": query_string, "type": "phrase"})
    # s = Search(index=index).query(q)

    query_string = request.GET.get('q', None)
    filters = {
        'portals': request.GET.getlist('portals', []),
        'clients': request.GET.getlist('clients', []),
        'categories': request.GET.getlist('categories', []),
    }

    s = WorklogSearch(query=query_string, filters=filters)
    pp = pprint.PrettyPrinter(indent=4)
    logger.debug(pp.pformat(s.build_search().to_dict()))

    paginator = Paginator(s, 25)
    page_no = request.GET.get('page')
    try:
        page = paginator.page(page_no)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    # search_results = s.execute()
    search_results = page.object_list.execute()

    template = 'search/serp.html'
    context = {
        'search_results': search_results.hits,
        'search_facets': search_results.facets,
        'search_count': search_results.hits.total,
        'query_string': query_string,
        'page_obj': page,
    }
    return render(request, template, context)
