from django.shortcuts import get_object_or_404, render
from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from elasticsearch_dsl import Search
from elasticsearch_dsl.query import Match


def serp(request):
    index = settings.ES_INDEX
    query_string = request.GET.get('q', None)

    q = Match(pwa_note={"query": query_string, "type": "phrase"})
    s = Search(index=index).query(q)

    # .query("match", pwa_note=query_string)

    paginator = Paginator(s, 25)
    page_no = request.GET.get('page')
    try:
        page = paginator.page(page_no)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    search_results = page.object_list.execute()
    # search_results = s.execute()

    template = 'search/serp.html'
    context = {
        'search_results': search_results.hits,
        'search_count': search_results.hits.total,
        'query_string': query_string,
        'page_obj': page,
    }
    return render(request, template, context)
