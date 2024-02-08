from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.TextField(max_length=50)
    
    password_usuario = models.TextField(max_length= 20)


class Lentes(models.Model):
    laboratorio = models.TextField(max_length=200)
    producto = models.TextField(max_length=200)
    codigo = models.IntegerField()
    indice = models.FloatField()
    precio = models.IntegerField()
    antireflejo = models.TextField(max_length=10)
    filtro_azul = models.TextField(max_length=10)
    fotocromatica = models.TextField(max_length=10)
    polarizado = models.TextField(max_length=10)
    esfera = models.FloatField()
    cilindro = models.FloatField()
    material = models.CharField(max_length=100, choices=[
        ('Policarbonato', 'Policarbonato'),
        ('Mineral', 'Mineral'),
        ('Organico', 'Orgánico'),
    ])

    def __str__(self):
        return str(self.codigo)
