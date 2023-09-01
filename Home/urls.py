from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('', views.home, name='home'),
    path('trabaja/', views.trabaja, name='trabaja'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_user, name='salir'),
    path('contacto/', views.contacto, name='contacto'),
    path('sobrenosotros/', views.sobreNosotros, name='Sobrenosotros'),
    path('en_construccion/', views.en_construccion, name='en_construccion'),
    path('register/', views.register, name='register'),

]

