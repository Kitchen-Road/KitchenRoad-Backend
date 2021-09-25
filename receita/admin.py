from django.contrib import admin
from .models import Categoria, Receita

# Register your models here.

admin.site.register(Receita)
admin.site.register(Categoria)
