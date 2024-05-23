from django.shortcuts import render

from territorios.forms import TerritorioForm

# Create your views here.
def agregarTerritorio(request):
    titulo="Territorio"
    form=TerritorioForm()
    context={
        
    }
    return render(request, "territoriosform/territoriosform.html", context)