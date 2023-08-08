from django.urls import path
from . import views

urlpatterns = [
    path('obras/', views.obras_user, name='obras'),
    path('categoria/<int:category_id>', views.category, name='categoria'),
]
