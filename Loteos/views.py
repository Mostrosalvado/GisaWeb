from django.shortcuts import render

# Create your views here.
def Lote (request):
        numeros= range(1,103)
        return render(request, "Lotes.html",{
        'title':'Lotes',
        'numeros':numeros
})

