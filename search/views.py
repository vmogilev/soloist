from django.shortcuts import get_object_or_404, render
from elasticsearch_dsl import Search, Q
from django.conf import settings


def serp(request):
    index = settings.ES_INDEX
    query_string = request.GET.get('q', None)

    s = Search(index=index) \
        .query("match", body=query_string)

    search_results = s.execute()

    template = 'search/serp.html'
    context = {
        'search_results': search_results.hits,
        'query_string': query_string,
    }
    return render(request, template, context)
