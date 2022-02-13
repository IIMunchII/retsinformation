from django.db import models
from scrapers.models import RetsinfoDocument

from .mixins import EmbeddingMixin


class DocumentEmbedding(EmbeddingMixin):
    document = models.OneToOneField(
        RetsinfoDocument, 
        on_delete=models.CASCADE, 
        related_name="document_embedding")


class SentenceEmbedding(EmbeddingMixin):
    document = models.ForeignKey(
        RetsinfoDocument, 
        on_delete=models.CASCADE, 
        related_name="sentence_embeddings")
