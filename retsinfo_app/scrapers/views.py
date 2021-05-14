"https://www.netlandish.com/blog/2020/06/22/full-text-search-django-postgresql/"

from django.http import Http404, JsonResponse
from .models import RetsinfoDocument
from django.contrib.postgres.search import SearchQuery

def search_documents(request):
    search_term = request.GET.get('search', None)
    limit = request.GET.get('limit', 10)
    if not search_term:
        raise Http404('Send a search term')

    documents = RetsinfoDocument.objects.filter(search_vector=SearchQuery(search_term, config='danish'))

    response_data = [
        {
            'title': doc.title,
            'short_name': doc.short_name,
            'ressort': doc.ressort,
        } for doc in documents[0:int(limit)]
    ]

    return JsonResponse(response_data, 
                        safe=False, 
                        json_dumps_params={'ensure_ascii':False, 'indent':4}, 
                        content_type='application/json; charset=utf-8')