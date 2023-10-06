from django.shortcuts import render, get_object_or_404, redirect
from .models import Lote
from rest_framework import generics
from .serializer_lote import LoteSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.decorators import login_required 
from django.contrib.auth import logout




# Create your views here.

# Vista para listar lotes
def Loteo (request):
        return render(request, "Lotes.html",{
        'title':'Lotes',
})


# Vista para buscar un lote por ID
def BuscaLote(request, id_lote=None):  
        if request.method == 'POST':
                id_lote = request.POST.get('id_lote')
                lote_encontrado = get_object_or_404(Lote, id_lote=id_lote)
                

                return render(request, 'Buscar_lote.html', {'lote_encontrado': lote_encontrado})
        else:
                # Si no es una solicitud POST, muestra el formulario vacío
                return render(request, 'Lotes.html')
        




# Vista para ver el lote propio del usuario autenticado
def Mi_lote(request):
        if request.user.is_authenticated:
                lote = Lote.objects.filter(user=request.user).first()
                if lote:
                        return render(request, "Mi_lote.html", {
                        'title': 'Mi Lote',
                        'lote': lote
                        })
                else:
                        no_lote_message = "No tienes ningún lote."
                        return render(request, "Mi_lote.html", {
                                'title': 'Mi Lote',
                                'no_authenticated_message': no_lote_message
        })
        else:
                # Si el usuario no está autenticado, configura una variable de contexto para mostrar un mensaje en la plantilla.
                no_authenticated_message = "Debe iniciar sesión para acceder a esta página."
                return render(request, "Lotes.html", {
                'title': 'Mi Lote',
                'no_authenticated_message': no_authenticated_message
})

# Vista para cerrar sesión de un usuario autenticado
@login_required(login_url="login")
def logout_user (request):
        logout(request)
        return redirect ('home')

# Vista basada en clase para listar y crear lotes a través de la API
class LoteListCreateView(generics.ListCreateAPIView):
        queryset = Lote.objects.all()
        serializer_class = LoteSerializer
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        permission_classes = [IsAuthenticated]

# Vista basada en clase para recuperar detalles de un lote específico por ID a través de la API
class LoteIdRetrieveView(generics.RetrieveAPIView):
        queryset = Lote.objects.all()
        serializer_class = LoteSerializer
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        permission_classes = [IsAuthenticated]

        def get_object(self):
                id_lote = self.kwargs['id_lote']
                return get_object_or_404(Lote, id_lote=id_lote)