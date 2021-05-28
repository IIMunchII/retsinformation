from django.http import Http404
from .models import RetsinfoDocument
from django.contrib.postgres.search import SearchQuery
from django.shortcuts import render
from .forms import SearchForm

def document_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = RetsinfoDocument.objects.filter(
                search_vector=SearchQuery(
                    query, config='danish'
                    )
                )
    return render(request, 
                  "documents/search_results.html", 
                  {"results": results[0:10],
                  "form": form,
                  "query": query})