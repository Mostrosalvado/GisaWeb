from django.urls import path
from . import views

urlpatterns = [
    path('obras/', views.obras_user, name='obras'),
    path('categoria/<int:category_id>', views.category, name='categoria'),
    path('api/obras/', views.LoteListCreateView.as_view(), name='lote-list-create'),
    path('api/obras/<int:id>/', views.LoteIdRetrieveView.as_view(), name='busca-lote'),
]



