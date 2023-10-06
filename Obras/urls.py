from django.urls import path
from . import views

urlpatterns = [
    # URL para ver las obras de un usuario
    path('obras/', views.obras_user, name='obras'),
    # URL para ver todas las obras
    path('obras_all/', views.obras, name='obras_all'),
    # URL para ver obras de una categoría específica por id
    path('categoria/<int:category_id>', views.category, name='categoria'),
    # URLs de la API para listar y crear obras
    path('api/obras/', views.ObraListCreateView.as_view(), name='obra-list-create'),
    # URL de la API para obtener detalles de una obra específica
    path('api/obras/<int:id>/', views.ObraIdRetrieveView.as_view(), name='busca-obra'),
]



