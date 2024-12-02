from django.urls import path

from .views import (
    cadastrar_noticia,
    categoria_cadastro,
    categoria_editar,
    categoria_excluir,
    categoria_listagem,
    editar_noticia,
    inicio_gerencia,
    listagem_noticia,
)

app_name = 'gerencia'

urlpatterns = [
    path('', inicio_gerencia, name='gerencia_inicial'),
    path('noticias/', listagem_noticia, name='listagem_noticia'),
    path('noticias/cadastro', cadastrar_noticia, name='cadastro_noticia'),
    path('noticias/editar/<int:id>', editar_noticia, name='editar_noticia'),
    # Add your URL patterns here
    path('categorias/', categoria_listagem, name='categoria_listagem'),
    path('categorias/cadastro', categoria_cadastro, name='categoria_cadastro'),
    path('categorias/editar/<int:id>', categoria_editar, name='categoria_editar'),
    path('categorias/excluir/<int:id>', categoria_excluir, name='categoria_excluir')
]