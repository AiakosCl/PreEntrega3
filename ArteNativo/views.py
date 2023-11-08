from typing import Any
from django.shortcuts import render, redirect
from .forms import ClienteForm, ProductoForm, VentasForm
import datetime
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ventas, Clientes, Productos
from django.contrib.humanize.templatetags.humanize import intcomma


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
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        for producto in context['productos']:
            producto.precio_formateado = intcomma(producto.precio).replace(',','.')
            producto.stock_formateado = intcomma(producto.stock).replace(",",".")
        
        return context

    
    
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