from django import forms
from .models import Cliente, Reserva, Quarto, Despesa, Receita
from django.contrib.auth.models import User

class ClienteForm (forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__' #importa todos o campos do model
        widgets = {
            'cpf': forms.TextInput(attrs={'placeholder' : '000.000.000-00'}),
            'telefone' : forms.TextInput(attrs={'placeholder' : '(99)99999-9999'})
            }
        
class ReservaForm (forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'

class QuartoForm(forms.ModelForm):
    class Meta:
        model = Quarto
        fields = '__all__'

class DespesaForm(forms.ModelForm):
    class Meta:
        model = Despesa
        fields = '__all__'

class ReceitaForm(forms.ModelForm):
    class Meta:
        model = Receita
        fields = '__all__'

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("As senhas não coincidem.")

        return cleaned_data
        