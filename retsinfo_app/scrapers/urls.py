from django.urls import path
from .views import document_search

app_name = 'scrapers'

urlpatterns = [
    path('search/', document_search, name='document_search'),
]