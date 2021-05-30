from django.db import models

class Embedding:
    def __init__(self, embedding, *args, **kwargs):
        self.embedding = embedding


class EmbeddingField(models.Field):
    description = "PostgreSQL cude type to represent embeddings of text"

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return Embedding(value.embedding)

    def to_python(self, value):
        if isinstance(value, Embedding):
            return value
        
        if value is None:
            return value
        return Embedding(value.embedding)

    def get_prep_value(self, value):
        return value.embedding
    
    def db_type(self, connection):
        return 'cube(float8)'