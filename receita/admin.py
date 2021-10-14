from django.contrib import admin
from .models import Categoria, Epoca, Receita

# Register your models here.

admin.site.register(Receita)
admin.site.register(Categoria)
admin.site.register(Epoca)
