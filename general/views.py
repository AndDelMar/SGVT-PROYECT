from django.shortcuts import render
def principales(request):
    titulo ="Bienvenido"
    context={
        "titulo": titulo,
    }
    return render(request, "index.html",context)