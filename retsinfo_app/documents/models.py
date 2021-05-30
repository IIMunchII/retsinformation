from django.db import models
from scrapers.models import RetsinfoDocument
from .fields import EmbeddingField

class DocumentEmbedding(models.Model):
    document = models.ForeignKey(
        RetsinfoDocument, 
        on_delete=models.CASCADE, 
        related_name="embeddings")
    embedding = EmbeddingField()