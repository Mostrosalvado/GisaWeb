from django.urls import path
from . import views

urlpatterns = [
    path('loteos/', views.Loteo, name='lote'),
    path('buscar_lote/<int:id_lote>/', views.BuscaLote, name='Buscar_lote'),
]
