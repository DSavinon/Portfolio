"""URL Patterns para Projects"""

from django.urls import path
from . import views

# app_name = "projects"

urlpatterns = [
    # Pagina Inicial.
    path("", views.index, name="index"),
    # Pagina de cada proyecto.
    path("<int:project_id>", views.detalles, name="detalles"),
    # Pagina para agregar.
    path("nuevo", views.nuevo_proyecto, name="nuevo_proyecto"),
]
