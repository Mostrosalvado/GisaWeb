from django.urls import path
from . import views

urlpatterns = [
    path('loteos/', views.Lote, name='lote'),
]
