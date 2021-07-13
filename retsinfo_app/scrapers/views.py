
from django.contrib.postgres.search import SearchQuery
from django.shortcuts import render
from django.views import View

from .forms import SearchForm
from .models import RetsinfoDocument
from documents.models import DocumentEmbedding
from documents.fields import Embedding
import requests

def document_search(request):
    form = SearchForm()
    query = None
    results = []

    if 'query' in request.POST:
        form = SearchForm(request.POST)
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

class NearestNeighborsView(View):

    def get(self, request):
        return render(request, 
                     "documents/search_results.html", 
                     {"results": [],
                     "form": SearchForm(),
                     "query": None})

    def post(self, request):
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            response = requests.post("http://127.0.0.1:5000/embed_and_reduce", data={"string": query})
            embedding_string = str(response.json()).rstrip("]").lstrip("[")
            embedding = Embedding(embedding_string)
            #embedding = DocumentEmbedding.objects.get(id=query).embedding
            queryset = DocumentEmbedding.search_nearest_neighbors(embedding)
            result = [item.document for item in queryset[0:10]]
            return render(request, 
                     "documents/search_results.html", 
                     {"results": result,
                     "form": form,
                     "query": query})