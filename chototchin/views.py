from django.shortcuts import render
from sabores.models import SaboresModel


def index (request):
    item = list(SaboresModel.objects.all())[-3:]
    contexto = {"produtos":item}
    return render(request, "index.html", contexto)

def story(request):
    return render(request, "story.html")

def people_we_love(request):
    return render(request, "people_we_love.html")