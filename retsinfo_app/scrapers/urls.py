from django.urls import path
from .views import document_search, NearestNeighborsView

app_name = 'scrapers'

urlpatterns = [
    path('search/', document_search, name='document_search'),
    path('nn_search/', NearestNeighborsView.as_view(), name='document_search')
]