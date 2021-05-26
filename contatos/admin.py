from django.contrib import admin
from .models import Categoria, Contato
# Register your models here.

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'mostrar')
    list_display_links = ('nome', 'sobrenome')
    list_per_page = 5
    search_fields = ('nome', 'sobrenome')
    list_editable = ('telefone', 'mostrar')


admin.site.register(Categoria)
admin.site.register(Contato, ContatoAdmin)
