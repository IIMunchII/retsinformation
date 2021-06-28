from django.contrib import admin
from .models import DocumentEmbedding, SentenceEmbedding

admin.site.register(DocumentEmbedding)
admin.site.register(SentenceEmbedding)