from django.urls import path
from . import views

urlpatterns = [
    path('export', views.create_pdf, name="export-pdf" ),
    path('image/', views.image, name="export-pdf" )
]
