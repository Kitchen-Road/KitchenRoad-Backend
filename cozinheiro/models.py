from django.db import models
from django.contrib.auth.models import AbstractUser
from receita.models import Receita

EXPERIENCIA = [
	('I','Iniciante'),
	('T','Intermediario'),
	('A','Avancado'),
]

class Cozinheiro(AbstractUser):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=100)
    #receitas_completadas = models.ManyToManyField(Receita)
    experiencia = models.CharField(max_length=1, choices=EXPERIENCIA, default='I')

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']