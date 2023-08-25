from django.shortcuts import render

# Create your views here.
def Lote (request):

    for i in range(1,103):   
        i=+1
        print(i)
#Arreglar
        return render(request, "Lotes.html",{
            'title':'Lotes',
            'i':i
    })

