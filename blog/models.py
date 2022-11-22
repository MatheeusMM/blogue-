from django.db import models


class Campo(models.Model):
    titulo = models.CharField(max_length=50)
    texto = models.TextField()
    imagem = models.ImageField(upload_to='imagens')
    hora = models.DateField(auto_now_add=True)


class usuario(models.Model):
    nome = models.CharField(max_length=50)