from django import forms
from app.models import Cliente, Marca, Ticket, Empleado, Producto

from django.forms import ModelForm

class ClientesForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ["cliente",]
        labels = {'cliente': 'Cliente',}

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = ["marca",]
        labels = {'marca': 'Marca',}

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ["ticket",]
        labels = {'ticket': 'Ticket',}

class EmpleadosForm(ModelForm):
    class Meta:
        model = Empleado
        fields = ["empleado",]
        labels = {'empleado': 'Empleado',}

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ["producto",]
        labels = {'producto': 'Producto',}