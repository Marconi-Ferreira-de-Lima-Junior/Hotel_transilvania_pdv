from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login as auth_login, authenticate, logout
from django.contrib.auth.models import User
from .models import Cliente, Reserva, Quarto, Despesa, Receita
from .forms import ClienteForm, DespesaForm, QuartoForm, ReceitaForm, ReservaForm, UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # Para exibir mensagens de erro

def login_view(request):
    if request.method == 'POST':  # Método POST para enviar as informações
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')  # Redireciona para o painel principal após o login
        else:
            # Exibe uma mensagem de erro se as credenciais forem inválidas
            messages.error(request, 'Usuário ou senha incorretos.')
            return render(request, 'pdv/login.html')  # Retorna para a página de login com mensagem de erro
    else:
        # Se o método não for POST, exibe o formulário de login
        return render(request, 'pdv/login.html')
    
def logout_view(request):
    logout(request)
    return redirect('login')  # Redireciona para a página de login após logout

def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'pdv/register.html', {'form':form}) 

#dashboard - reservas e ocupação
@login_required
def dashboard(request):
    total_clientes = Cliente.objects.count()
    total_reserva = Reserva.objects.count()
    quartos_disponiveis = Quarto.objects.filter(disponivel=True).count()#filtra os quartos disponiveis

    return render(request,'pdv/dashboard.html', {
        'total_clientes':total_clientes,
        'total_reserva':total_reserva,
        'quartos_disponiveis':quartos_disponiveis   
    })

#listando os clientes
@login_required
def clientes_view(request):
    clientes = Cliente.objects.all()
    return render(request, 'pdv/clientes.html', {'clientes':clientes})

#cadastro de clientes
@login_required
def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm()
    
    return render(request, 'pdv/cadastrar_cliente.html', {'form':form})

@login_required
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente) #cria um formulario preenchido com os dados novos dos clientes que foram enviados pelo usuario, referenciando ao cliente que ja existe  instance = cliente
        if form.is_valid():
            form.save()
            return redirect('clientes')
    else:
        form = ClienteForm(instance=cliente)

    return render (request, 'pdv/editar_cliente.html', {'form': form})


@login_required 
def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method =='POST':
        cliente.delete()
        return redirect('clientes')
    return render (request, 'pdv/confirmar_exclusao.html', {'cliente':cliente})

#reservas - listar as reservas existentes
@login_required
def reservas_view(request):
    reservas = Reserva.objects.all()
    return render (request, 'pdv/reservas.html',{'reservas':reservas})

#criar as reservas
@login_required
def criar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reservas')
    else:
        form = ReservaForm()

    return render (request, 'pdv/criar_reserva.html', {'form':form})

@login_required
def editar_reserva(request,id):
    reserva = get_object_or_404(Reserva, id=id)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance = reserva)
        if form.is_valid():
            form.save()
            return redirect ('reservas')
    else:
        form = ReservaForm(instance = reserva)
    return render (request, 'pdv/editar_reserva.html', {'form':form})

@login_required
def excluir_reserva(request,id):
    reserva = get_object_or_404(Reserva, id = id)
    if request.method == 'POST':
        reserva.delete()
        return redirect('reservas')
    return render (request, 'pdv/confirmar_exclusao.html', {'reserva': reserva})

#faturamento total do hotel
@login_required
def relatorios_view(request):
    total_receitas = sum(receita.valor for receita in Receita.objects.all())
    total_despesas = sum(despesa.valor for despesa in Despesa.objects.all())
    saldo_total = total_receitas - total_despesas

    return render (request, 'pdv/relatorios.html', {
        'total_receitas':total_receitas,
        'total_despesas':total_despesas,
        'saldo_total':saldo_total
    })

@login_required
def cadastrar_quarto(request):
    if request.method == 'POST':
        form = QuartoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('quartos')
    else:
        form = QuartoForm()
    return render (request, 'pdv/cadastrar_quarto.html', {'form':form})

@login_required
def cadastrar_despesas(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relatorios') #direcionar para relatorios
    else:
        form = DespesaForm()

    return render (request, 'pdv/cadastrar_despesas.html', {'form':form})

@login_required
def cadastrar_receitas(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relatorios')

    else:
        form = ReceitaForm()

    return render(request, 'pdv/cadastrar_receitas.html', {'form':form})
    
def listar_quartos(request):
    quartos = Quarto.objects.all()
    return render(request, 'pdv/quartos/listar.html', {'quartos': quartos})


# Listar despesas
@login_required
def listar_despesas(request):
    despesas = Despesa.objects.all()
    return render(request, 'pdv/despesas/listar.html', {'despesas': despesas})

# Editar despesa
@login_required
def editar_despesa(request, id):
    despesa = get_object_or_404(Despesa, id=id)
    if request.method == 'POST':
        form = DespesaForm(request.POST, instance=despesa)
        if form.is_valid():
            form.save()
            return redirect('listar_despesas')
    else:
        form = DespesaForm(instance=despesa)
    return render(request, 'pdv/despesas/editar.html', {'form': form})

# Excluir despesa
@login_required
def excluir_despesa(request, id):
    despesa = get_object_or_404(Despesa, id=id)
    if request.method == 'POST':
        despesa.delete()
        return redirect('listar_despesas')
    return render(request, 'pdv/despesas/confirmar_exclusao.html', {'despesa': despesa})

# Listar receitas
@login_required
def listar_receitas(request):
    receitas = Receita.objects.all()
    return render(request, 'pdv/receitas/listar.html', {'receitas': receitas})

# Editar receita
@login_required
def editar_receita(request, id):
    receita = get_object_or_404(Receita, id=id)
    if request.method == 'POST':
        form = ReceitaForm(request.POST, instance=receita)
        if form.is_valid():
            form.save()
            return redirect('listar_receitas')
    else:
        form = ReceitaForm(instance=receita)
    return render(request, 'pdv/receitas/editar.html', {'form': form})

# Excluir receita
@login_required
def excluir_receita(request, id):
    receita = get_object_or_404(Receita, id=id)
    if request.method == 'POST':
        receita.delete()
        return redirect('listar_receitas')
    return render(request, 'pdv/receitas/confirmar_exclusao.html', {'receita': receita})

# Editar quarto
@login_required
def editar_quarto(request, id):
    quarto = get_object_or_404(Quarto, id=id)
    if request.method == 'POST':
        form = QuartoForm(request.POST, instance=quarto)
        if form.is_valid():
            form.save()
            return redirect('listar_quartos')
    else:
        form = QuartoForm(instance=quarto)
    return render(request, 'pdv/quartos/editar.html', {'form': form})

# Excluir quarto
@login_required
def excluir_quarto(request, id):
    quarto = get_object_or_404(Quarto, id=id)
    if request.method == 'POST':
        quarto.delete()
        return redirect('listar_quartos')
    return render(request, 'pdv/quartos/confirmar_exclusao.html', {'quarto': quarto})



