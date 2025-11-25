
from django import forms
from .models import SaboresModel


class SaboresForm(forms.ModelForm):
    class Meta:
        model = SaboresModel
        fields = ["nome_produto", "descricao_produto", "descricao_produto_pequena",  "preco_produto", "titulo_musica_produto", "letra_musica_produto", "musica_produto",  "embalagem_produto", "fundo_descricao_produto", "mascote_parado_produto", "mascote_dancando_produto", "mascote_letras_produto", "tabela_nutricional_produto", "ingrediente_pendurado_produto", "barra_produto" ]
        widgets = {
            "nome_produto": forms.TextInput(attrs={"class": "formulario_controle", "placeholder": "Digite aqui o nome do produto"}),
            "descricao_produto": forms.Textarea(attrs={"class": "formulario_controle", "placeholder":"Digite a descrição do produto"}),
            "embalagem_produto": forms.FileInput(attrs={"class:":"embalagem_produto"}),
            "preco_produto": forms.NumberInput(attrs={"class":"formulario_controle", "default":2.99}),
            "titulo_musica_produto": forms.Textarea(attrs={"class": "formulario_controle", "placeholder":"Digite o titulo da música"}),
            "letra_musica_produto": forms.Textarea(attrs={"class": "formulario_controle", "placeholder":"Digite a letra da música"})
        }
        labels = {'nome_produto':'Nome do Produto', 'descricao_produto':'Descrição do Produto', "embalagem_produto":'Embalagem do Produto', "preco_produto":'Preço do Chocotchin', "fundo_descricao_produto": "Imagem do Fundo da Descrição", "mascote_parado_produto": "Imagem do Mascote Parado", "mascote_dancando_produto": "Sprite do Mascote Dançando", "mascote_letras_produto":"Imagem do Mascote com Partitura", "tabela_nutricional_produto":"Imagem da Tabela Nutricional", "ingrediente_pendurado_produto":"Ingrediente Pendurado", "letra_musica_produto":"Letra da Música", "titulo_musica_produto":"Título da música", "musica_produto":"Música", "barra_produto":"Barra de Promoção", "descricao_produto_pequena": "Descrição Breve"}