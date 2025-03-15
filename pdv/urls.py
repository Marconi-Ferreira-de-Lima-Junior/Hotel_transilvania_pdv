from django.urls import path
from .views import (
    login_view, logout_view, register_view, dashboard,
    clientes_view, cadastrar_cliente, editar_cliente, excluir_cliente,
    reservas_view, criar_reserva, editar_reserva, excluir_reserva,
    relatorios_view, cadastrar_quarto, cadastrar_despesas, editar_despesa, excluir_despesa,
    cadastrar_receitas, editar_receita, excluir_receita, listar_quartos, detalhes_quarto
)

urlpatterns = [
    # Login, Logout e Registro
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register_view, name='register'),

    # Dashboard
    path('dashboard/', dashboard, name='dashboard'),

    # Clientes
    path('clientes/', clientes_view, name='clientes'),
    path('clientes/novo/', cadastrar_cliente, name='cadastrar_cliente'),
    path('clientes/editar/<int:id>/', editar_cliente, name='editar_cliente'),
    path('clientes/excluir/<int:id>/', excluir_cliente, name='excluir_cliente'),

    # Reservas
    path('reservas/', reservas_view, name='reservas'),
    path('reservas/novo/', criar_reserva, name='criar_reserva'),
    path('reservas/editar/<int:id>/', editar_reserva, name='editar_reserva'),
    path('reservas/excluir/<int:id>/', excluir_reserva, name='excluir_reserva'),

    # Relatórios
    path('relatorios/', relatorios_view, name='relatorios'),

    # Quartos
    path('quartos/', listar_quartos, name='listar_quartos'),
    path('quartos/<int:id>/', detalhes_quarto, name='detalhes_quarto'),
    path('quartos/novo/', cadastrar_quarto, name='cadastrar_quarto'),

    # Despesas
    path('despesas/nova/', cadastrar_despesas, name='cadastrar_despesas'),
    path('despesas/editar/<int:id>/', editar_despesa, name='editar_despesa'),
    path('despesas/excluir/<int:id>/', excluir_despesa, name='excluir_despesa'),

    # Receitas
    path('receitas/nova/', cadastrar_receitas, name='cadastrar_receitas'),
    path('receitas/editar/<int:id>/', editar_receita, name='editar_receita'),
    path('receitas/excluir/<int:id>/', excluir_receita, name='excluir_receita'),
]