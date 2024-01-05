from django.db import models

class VideoJuegos(models.Model):

    nombre = models.CharField(max_length=20)
    desarrolladora = models.CharField(max_length=20)
    stock = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}"

class Libros(models.Model):

    nombre = models.CharField(max_length=20)
    autor = models.CharField(max_length=20)
    stock = models.IntegerField() 

    def __str__(self):
        return f"{self.nombre}"

class Peliculas(models.Model):

    nombre = models.CharField(max_length=20)
    director = models.CharField(max_length=20)
    stock = models.IntegerField()    

    def __str__(self):
        return f"{self.nombre}" 
