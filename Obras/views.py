from django.shortcuts import render
from Obras.models import Category, Obra
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from rest_framework import generics
from .serializer_obras import ObraSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.


@login_required(login_url="login")
def obras_user(request):
    # Sacar obras del usuario logueado
    obras = Obra.objects.filter(user=request.user)

    return render(request, "obras.html", {
        'title': 'Mi obra',
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

class ObraListCreateView(generics.ListCreateAPIView):
        queryset = Obra.objects.all()
        serializer_class = ObraSerializer
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        permission_classes = [IsAuthenticated]


class ObraIdRetrieveView(generics.RetrieveAPIView):
        queryset = Obra.objects.all()
        serializer_class = ObraSerializer
        authentication_classes = [SessionAuthentication, BasicAuthentication]
        permission_classes = [IsAuthenticated]

        def get_object(self):
                id_obra = self.kwargs['id']
                return get_object_or_404(Obra, id=id_obra)
        