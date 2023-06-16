from http import client
from django.contrib import admin
from .models import Producto, Empleado, Cliente, Ticket, Marca

# Register your models here.
admin.site.register(Producto)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Ticket)
admin.site.register(Marca)


