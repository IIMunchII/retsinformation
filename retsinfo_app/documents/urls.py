from django.urls import path
from . import views

app_name = 'documents'

urlpatterns = [
    path('/<int:id>/<int:doc_id>/', views.document_detail, name='document_detail'),
]