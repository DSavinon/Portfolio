from django.db import models

# Create your models here.


class Project(models.Model):
    imagen = models.ImageField(upload_to="images/")
    nombre = models.CharField(max_length=100)
    resumen = models.CharField(max_length=200)
    git_rep = models.URLField(default="https://github.com/DSavinon", max_length=200)
    project_link = models.URLField(
        default="https://github.com/DSavinon", max_length=200
    )

    def __str__(self) -> str:
        return self.resumen
