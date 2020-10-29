from django.contrib import admin
from django.urls import path

from .views import IngestDataAPIView


app_name = "apis"

urlpatterns = [
    path('ingest', IngestDataAPIView.as_view(), name="ingest-data"),
]
