from django.db import models
from django.contrib.postgres.search import SearchVectorField, SearchVector
from .managers import RetsinfoDocumentManager
from django.contrib.postgres.indexes import GinIndex
from django.urls import reverse

class RetsinfoDocument(models.Model):
    class Meta:
        indexes = [GinIndex(fields=["search_vector"])]

    doc_id = models.IntegerField()
    url = models.URLField()
    title = models.TextField()
    short_name = models.CharField(max_length=500)
    document_text = models.TextField()
    document_html = models.TextField()
    search_vector = SearchVectorField()
    is_historical = models.BooleanField()
    ressort = models.CharField(max_length=255)
    is_reprint = models.BooleanField()
    geographic_id = models.IntegerField()
    retsinfo_klassifikation_id = models.IntegerField()
    has_fob_tags = models.BooleanField()
    metadata = models.JSONField()
    editorial_notes = models.JSONField()
    alternative_media = models.JSONField()
    document_year = models.IntegerField()
    document_nr = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('documents:document_detail',
                       args=[self.id, self.doc_id])
                             

    def save(self, *args, **kwargs):
        self.search_vector = SearchVector('document_text') 
        super().save(*args, **kwargs)
    
    objects = RetsinfoDocumentManager()


class RetsinfoSentences(models.Model):
    document = models.ForeignKey(RetsinfoDocument, 
                                 on_delete=models.CASCADE,
                                 related_name="sentences")
    sentence_text = models.TextField()