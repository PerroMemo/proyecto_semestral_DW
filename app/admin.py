from http import client
from django.contrib import admin
from .models import Producto, Empleado, Cliente, Boleta, Marca

# Register your models here.
admin.site.register(Producto)
admin.site.register(Empleado)
admin.site.register(Cliente)
admin.site.register(Boleta)
admin.site.register(Marca)


