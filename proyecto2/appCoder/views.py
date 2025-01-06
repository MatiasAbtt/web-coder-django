from django.shortcuts import render
from .models import Curso

# Create your views here.


def cursos(request):

    cursos = Curso.objects.all()

    contexto = {"cursos": cursos}
    return render(request, "cursos.html", contexto)