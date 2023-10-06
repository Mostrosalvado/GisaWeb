from django.urls import path
from . import views


urlpatterns = [
    # URL para listar y crear lotes
    path('loteos/', views.Loteo, name='lote'),
    # URL para buscar un lote específico por ID
    path('buscar_lote/<int:id_lote>/', views.BuscaLote, name='Buscar_lote'),
    # URLs de la API para listar y crear lotes
    path('api/lotes/', views.LoteListCreateView.as_view(), name='lote-list-create'),
    # URLs de la API para recuperar detalles de un lote específico por ID
    path('api/lotes/<int:id_lote>/', views.LoteIdRetrieveView.as_view(), name='busca-lote'),
    # URL para ver el lote propio del usuario autenticado
    path('mi_lote/', views.Mi_lote, name='mi_lote'),
    # URL para cerrar sesión
    path('logout/', views.logout_user, name='salir'),
]
