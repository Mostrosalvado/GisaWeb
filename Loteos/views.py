from django.shortcuts import render, get_object_or_404
from .models import Lote
#from django.shortcuts import get_object_or_404




# Create your views here.
def Loteo (request):
        return render(request, "Lotes.html",{
        'title':'Lotes',
})



def BuscaLote(request, id_lote=None):  
        if request.method == 'POST':
                id_lote = request.POST.get('id_lote')
                lote_encontrado = get_object_or_404(Lote, id_lote=id_lote)
                

                return render(request, 'Buscar_lote.html', {'lote_encontrado': lote_encontrado})
        else:
                # Si no es una solicitud POST, muestra el formulario vacío
                return render(request, 'Lotes.html')
