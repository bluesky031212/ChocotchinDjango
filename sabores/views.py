from django.shortcuts import render, redirect
from .forms import SaboresForm
from django.contrib import messages


# Create your views here.
def cadastrar_sabores(request):
    if request.method == "POST":
        formulario = SaboresForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "O chocotchin foi cadastrado com sucesso!!!")
            return redirect("cadastrar_sabores")
        else:
        # Se for GET, cria um formulário vazio
            formulario = SaboresForm()
    contexto = {"forms":SaboresForm}
    return render(request, "adicionar/cadastrar_sabores.html", contexto)


def almond(request):
    return render(request, "sabores/almond.html")