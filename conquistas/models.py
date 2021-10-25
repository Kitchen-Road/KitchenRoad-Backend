from django.db import models

# Create your models here.


class Conquista(models.Model):
    nome_conquista = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='post_img')
    descrição_conquista = models.TextField()

    def __str__(self):
        return self.nome_conquista
