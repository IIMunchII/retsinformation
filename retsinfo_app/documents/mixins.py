from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.indexes import GinIndex

from .fields import EmbeddingField, Embedding


class EmbeddingMixin(models.Model):
    class Meta:
        abstract = True
        indexes = [GinIndex(fields=["embedding"])]

    embedding = EmbeddingField(null=True, blank=True)
    array = ArrayField(models.FloatField(), default=list)

    @classmethod
    def search_nearest_neighbors(cls, embedding: Embedding):
        table_name = cls.objects.model._meta.db_table
        return cls.objects.raw(cls.get_nn_query(table_name), [embedding.tolist()])

    @staticmethod
    def get_nn_query(table_name):
        return f"SELECT * FROM {table_name} ORDER BY embedding <-> cube(%s)"
