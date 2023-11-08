from django import forms
from .models import Clientes, Productos, Ventas

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Clientes
        fields = '__all__'

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = '__all__'

class VentasForm(forms.ModelForm):
    class Meta:
        model = Ventas
        fields = '__all__'