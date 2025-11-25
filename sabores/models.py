from django.db import models

# Create your models here.

class SaboresModel(models.Model):
    nome_produto = models.CharField(max_length=50)
    embalagem_produto = models.ImageField(upload_to="sabores/embalagens", null=True, blank=True)
    fundo_descricao_produto = models.ImageField(upload_to="sabores/fundo_descricao", null=True, blank=True)
    mascote_parado_produto = models.ImageField(upload_to="sabores/mascote", null=True, blank=True)
    mascote_dancando_produto = models.ImageField(upload_to="sabores/mascote", null=True, blank=True)
    mascote_letras_produto = models.ImageField(upload_to="sabores/mascote", null=True, blank=True)
    barra_produto = models.ImageField(upload_to="sabores/barras", null=True, blank=True)
    tabela_nutricional_produto = models.ImageField(upload_to="sabores/tabela_nutricional", null=True, blank=True)
    ingrediente_pendurado_produto = models.ImageField(upload_to="sabores/ingrediente_pendurado", null=True, blank=True)
    titulo_musica_produto = models.CharField(max_length=50)
    letra_musica_produto = models.TextField()
    musica_produto = models.FileField(upload_to="sabores/musica", null=True, blank=True)
    descricao_produto = models.TextField()
    descricao_produto_pequena = models.TextField()
    preco_produto = models.FloatField()

    def __str__(self):
        return self.nome_produto