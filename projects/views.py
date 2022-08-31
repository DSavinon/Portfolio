from django.shortcuts import render, get_object_or_404, redirect

from .models import Project

# Create your views here.


def index(request):
    """Pagina de Inicio"""

    project_obj = Project.objects.all()
    project_dict = {"projects": project_obj}

    return render(request, "projects/index.html", context=project_dict)


def detalles(request, project_id):
    """Pagina con la Descripcion de los Proyectos"""

    detalle_proyecto = get_object_or_404(Project, pk=project_id)
    return render(request, "projects/detalles.html", {"project": detalle_proyecto})


def nuevo_proyecto(request):
    return render(request, "projects/nuevo_proyecto.html")
