from django.shortcuts import render

from .models import Ganador

# Create your views here.
def caso_list(request):
    ganadores = Ganador.objects.all()

    context = {
        "ganadores" : ganadores,
    }

    return render(request, "ganador/ganador_list.html",  context)