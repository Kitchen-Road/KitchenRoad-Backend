from django.db import models

DIFICULDADES_ESCOLHAS = [
    ('I', 'Iniciante'),
    ('T', 'Intermediario'),
    ('A', 'Avancado'),
]


class Categoria(models.Model):
    nome_categoria = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_categoria


class Epoca(models.Model):
    nome_epoca = models.CharField(max_length=50)

    def __str__(self):
        return self.nome_epoca


class Receita(models.Model):
    nome_receita = models.CharField(unique=True, max_length=50)
    imagem = models.ImageField(upload_to='post_img')
    link_video_receita = models.URLField()
    categoria_receita = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    ingredientes = models.TextField(default="1.")
    modo_preparo = models.TextField()
    dificuldade = models.CharField(max_length=1, choices=DIFICULDADES_ESCOLHAS)
    epoca = models.ForeignKey(Epoca, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_receita
