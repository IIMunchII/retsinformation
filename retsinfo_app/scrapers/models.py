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
    document_year = models.IntegerField()
    document_nr = models.IntegerField()


class RetsinfoRequestLog(models.Model):
    # Request fields
    url = models.URLField()
    method = models.CharField(max_length=10)
    headers = models.JSONField()
    meta = models.JSONField()
    priority = models.IntegerField()
    encoding = models.CharField(max_length=25)
    document_year = models.IntegerField()
    document_nr = models.IntegerField()
    # Response fields
    status = models.IntegerField()
    ip_address = models.GenericIPAddressField()
    protocol = models.CharField(max_length=10)
    log_timestamp = models.DateTimeField(auto_now=True)