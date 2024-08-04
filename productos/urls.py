from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name='productos'),
   path('view/<int:id>', views.view, name='producto_view'),
   path('edit/<int:id>', views.edit, name='producto_edit'),
   path('scan/', views.scan_barcode, name='scan_barcode'),
   path('create/', views.create, name='producto_create'),
    path('delete/<int:id>', views.delete, name='producto_delete'),
]
