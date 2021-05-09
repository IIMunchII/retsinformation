from django.db import models

class RetsinfoDocument(models.Model):
    doc_id = models.IntegerField()
    title = models.TextField()
    short_name = models.CharField(max_length=500)
    document_text = models.TextField()
    document_html = models.TextField()
    is_historical = models.BooleanField()
    ressort = models.CharField(max_length=255)
    is_reprint = models.BooleanField()
    geographic_id = models.IntegerField()
    retsinfo_klassifikation_id = models.IntegerField()
    has_fob_tags = models.BooleanField()
    metadata = models.JSONField()
    editorial_notes = models.JSONField()
    alternative_media = models.JSONField()
