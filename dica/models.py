from django.db import models

DIFICULDADES_ESCOLHAS = [
	('F','Fácil'),
	('M','Médio'),
	('D','Difícil'),
]

class Dica(models.Model):
    titulo = models.CharField(max_length=100)
    conteudo_dica = models.TextField()
    dificuldade = models.CharField(max_length=1, choices=DIFICULDADES_ESCOLHAS)
    def __str__(self):
        return self.titulo