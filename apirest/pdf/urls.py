from django.urls import path
from . import views

urlpatterns = [
    path('export', views.create_pdf, name="export-pdf" ),
    path('image/', views.image, name="export-pdf" ),

    path('render/', views.render_pdf_view, name="export-pdf" ),
    path('customer/', views.CustomerListView.as_view(), name="customer-pdf" ),
    path('customer/<int:pk>', views.customer_render_pdf_view, name="customer-export-pdf" ),
]
