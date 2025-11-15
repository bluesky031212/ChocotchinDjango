from django.shortcuts import render, redirect, get_object_or_404
from .forms import SaboresForm
from django.contrib import messages
from .models import SaboresModel


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


def sabores(request, id):
    contexto = get_object_or_404(SaboresModel, id=id)
    return render(request, "sabores/sabores.html", {"produto":contexto})