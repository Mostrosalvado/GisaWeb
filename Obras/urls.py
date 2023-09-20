from django.urls import path
from . import views

urlpatterns = [
    path('obras/', views.obras_user, name='obras'),
    path('categoria/<int:category_id>', views.category, name='categoria'),
    path('api/obras/', views.ObraListCreateView.as_view(), name='obra-list-create'),
    path('api/obras/<int:id>/', views.ObraIdRetrieveView.as_view(), name='busca-obra'),
]



