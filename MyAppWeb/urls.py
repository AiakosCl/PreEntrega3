"""
URL configuration for MyAppWeb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ArteNativo import views

app_label = 'ArteNativo'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('index/', views.index, name='inicio'),
    path('clientes/', views.Cliente_form, name='cliente_form'),  # Cambiado el nombre de la URL
    path('productos/agregar/', views.Producto_form, name='producto_form'),
    path('ventas/', views.Ventas_form, name='ventas_form'),  # Cambiado el nombre de la URL
    path('productos/', views.ProductoListView.as_view(), name='producto_lista'),
]

