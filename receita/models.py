from django.db import models

DIFICULDADES_ESCOLHAS = [
	('F','Fácil'),
	('M','Médio'),
	('D','Difícil'),
]

class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50)
    def __str__(self):
        return self.nome_categoria

class Receita(models.Model):
    nome_receita = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='post_img')
    link_video_receita = models.URLField()
    categoria_receita = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    modo_preparo = models.TextField()
    dificuldade = models.CharField(max_length=1, choices=DIFICULDADES_ESCOLHAS)
    def __str__(self):
        return self.nome_receita