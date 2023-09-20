from django.shortcuts import render, redirect
from Obras.models import Category, Obra
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from rest_framework import generics
from .serializer_obras import ObraSerializer


# Create your views here.
'''
def obras (request):
    
    #Sacar obras
    obras=Obra.objects.all()
    #Paginar obras
    paginacion=Paginator(obras,3)
    #Obtener numero de pagina
    page = request.GET.get('page')
    page_obras= paginacion.get_page(page)

    return render(request, "home.html",{
        'title':'Obras',
        'obras':page_obras
    })
'''

@login_required(login_url="login")
def obras_user(request):
    # Sacar obras del usuario logueado
    obras = Obra.objects.filter(user=request.user)

    return render(request, "home.html", {
        'title': 'Inicio',
        'obras': obras
    })

def category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    obras = Obra.objects.filter(category = category_id)
    

    return render(request, 'category.html', {
        'category': category,
        'obras': obras,
        'title': category.name
    })

class LoteListCreateView(generics.ListCreateAPIView):
        queryset = Obra.objects.all()
        serializer_class = ObraSerializer


class LoteIdRetrieveView(generics.RetrieveAPIView):
        queryset = Obra.objects.all()
        serializer_class = ObraSerializer

        def get_object(self):
                id_obra = self.kwargs['id']
                return get_object_or_404(Obra, id=id_obra)