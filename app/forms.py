from django import forms
from app.models import Cliente, Marca, Boleta, Empleado, Producto

from django.forms import ModelForm

class ClientesForm(ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"

class MarcaForm(ModelForm):
    class Meta:
        model = Marca
        fields = "__all__"

class BoletaForm(ModelForm):
    class Meta:
        model = Boleta
        fields = "__all__"

class EmpleadosForm(ModelForm):
    class Meta:
        model = Empleado
        fields = "__all__"

class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = "__all__"

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        if not imagen:
            return None
        return imagen

class RegistroForm(ModelForm):
    class Meta:
        model = Cliente
        fields = "__all__"