import numpy as np
from django.db import models


class CubeValue(models.Transform):
    lookup_name = 'cube'
    function = 'CUBE'

class NearestNeighbors(models.Lookup):
    """
    Used to find nearest neighbors by euclidian distance.
    The lookup is performed by GIST index.
    """
    lookup_name = 'nn'

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params
        return '%s <-> cube(%s)' % (lhs, rhs), params

class Embedding:
    def __init__(self, db_value: str, *args, **kwargs):
        self.__array = self.__to_np_array(db_value)

    def __to_np_array(self, db_value: str):
        clean_string = self.clean_string(db_value)
        return np.fromstring(clean_string, sep=',')

    def clean_string(self, db_value):
        return db_value.rstrip(')').lstrip('(')

    def tolist(self):
        return self.array.tolist()
    
    @property
    def array(self):
        return self.__array

    def __str__(self):
        return self.__repr__()
    
    def __repr__(self):
        return repr(self.array.tolist())


class EmbeddingField(models.Field):
    description = "PostgreSQL cube type to represent embeddings of text"

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return Embedding(value)

    def to_python(self, value):
        if isinstance(value, Embedding):
            return value
        
        if value is None:
            return value
        return Embedding(value)

    def get_prep_value(self, value):
        return value.array
    
    def db_type(self, connection):
        return 'cube'
