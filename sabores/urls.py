from django.urls import path
from. import views

urlpatterns = [
    path("cadastrar_sabores", views.cadastrar_sabores, name="cadastrar_sabores"),
    path("<int:id>/", views.sabores, name="sabores")

]