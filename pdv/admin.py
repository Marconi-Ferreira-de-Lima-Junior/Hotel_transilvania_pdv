from django.contrib import admin
from .models import Cliente, Quarto, Reserva, Despesa, Receita

#registrando os modelos para que apareçam no painel de administração

admin.site.register(Cliente)
admin.site.register(Quarto)
admin.site.register(Reserva)
admin.site.register(Despesa)
admin.site.register(Receita)
