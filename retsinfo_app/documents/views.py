from django.shortcuts import render
from scrapers.models import RetsinfoDocument

def document_detail(request, id, doc_id):

    if request.method == 'GET':
        document = RetsinfoDocument.objects.get(id=id, 
                                                doc_id=doc_id)

    return render(request,
                  'documents/detail.html',
                  {'document': document,})