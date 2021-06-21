from django.db import models
from scrapers.models import RetsinfoDocument

from .fields import EmbeddingField
from django.contrib.postgres.fields import ArrayField

class DocumentEmbedding(models.Model):
    document = models.OneToOneField(
        RetsinfoDocument, 
        on_delete=models.CASCADE, 
        related_name="document_embedding")
    embedding = EmbeddingField()
    array = ArrayField(models.FloatField(), default=list)

class SentenceEmbedding(models.Model):
    document = models.ForeignKey(
        RetsinfoDocument, 
        on_delete=models.CASCADE, 
        related_name="sentence_embeddings")
    embedding = EmbeddingField()
    array = ArrayField(models.FloatField(), default=list)