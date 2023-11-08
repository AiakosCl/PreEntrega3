from django.shortcuts import render, redirect
from .forms import ClienteForm, ProductoForm, VentasForm
import datetime
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ventas, Clientes, Productos


def index(request):
    return render(request, 'index.html')

def Cliente_form(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'cliente_form.html', {'form': form})
    

class ProductoListView(ListView):
    model = Productos
    template_name = "producto_lista.html"
    context_object_name = 'productos'
    
    
def Producto_form(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return (redirect('index'))
        
    else:
        form = ProductoForm()
    
    return render(request, 'Producto_form.html', {'form':form})

def Ventas_form(request):
    if request.method == 'POST':
        form = VentasForm(request.POST)
        if form.is_valid():
            venta = form.save(commit=False)
            venta.total = venta.producto.precio * venta.cantidad
            venta.save()
            return redirect('index')
    else:
        form = VentasForm()
    return render(request, 'Ventas_form.html', {'form':form})