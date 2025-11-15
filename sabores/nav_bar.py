from .models import SaboresModel

def nav_bar_sabores(request):
    sabores_nav = SaboresModel.objects.values("nome_produto", "id")
    return {"produtos_nav":sabores_nav}