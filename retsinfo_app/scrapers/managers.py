from django.contrib.postgres.aggregates import StringAgg
from django.contrib.postgres.search import (
    SearchQuery, SearchRank, SearchVector, TrigramSimilarity,
)
from django.db import models

class RetsinfoDocumentManager(models.Manager):
    def search(self, search_text):

        search_query = SearchQuery(
            search_text, config='danish'
        )

        qs = (self.get_queryset()
                  .filter(search_vector=search_query)
        )
        return qs