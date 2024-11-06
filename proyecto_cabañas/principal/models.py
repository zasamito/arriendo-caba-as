from django.db import models

class Comentario(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()
    comentario = models.TextField()

    def __str__(self):
        return f'Comentario de {self.nombre}'