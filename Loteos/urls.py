from django.urls import path
from . import views

urlpatterns = [
    path('loteos/', views.Loteo, name='lote'),
    path('buscar_lote/<int:id_lote>/', views.BuscaLote, name='Buscar_lote'),
    path('api/lotes/', views.LoteListCreateView.as_view(), name='lote-list-create'),
    path('api/lotes/<int:id_lote>/', views.LoteIdRetrieveView.as_view(), name='busca-lote'),
]
