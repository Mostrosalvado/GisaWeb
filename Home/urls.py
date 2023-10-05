from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'), # Ruta para la página de inicio
    path('', views.home, name='home'), # Ruta de inicio (página de inicio)
    path('login/', views.login_page, name='login'), # Ruta para la página de inicio de sesión
    path('logout/', views.logout_user, name='salir'), # Ruta para la página de cierre de sesión
    path('contacto/', views.contacto, name='contacto'), # Ruta para la página de contacto
    path('sobrenosotros/', views.sobreNosotros, name='Sobrenosotros'), # Ruta para la página "Sobre Nosotros"
    path('register/', views.register, name='register'), # Ruta para la página de registro de usuarios

]

