from django.apps import AppConfig
from django.db import models
from .fields import NearestNeighbors

class DocumentsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'documents'

    def ready(self):
        models.Field.register_lookup(NearestNeighbors)