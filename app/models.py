from django.db import models
from django.utils import timezone

# Create your models here.


class Marca(models.Model):
    id_marca        = models.AutoField(db_column='idMarca', primary_key=True)  
    nombre           = models.CharField(max_length=20)

    def __str__(self):
        return str(self.nombre)

class Producto(models.Model):
    id              = models.AutoField(primary_key=True)
    nombre          = models.CharField(max_length=20)
    precio          = models.IntegerField()
    id_marca        = models.ForeignKey('Marca',on_delete=models.CASCADE, db_column='idMarca')  
    stock           = models.IntegerField()
    imagen          = models.ImageField(upload_to='app/static/media', blank=True, null=True)

    def __str__(self):
        return str(self.id) + " " + str(self.nombre)+" "+str(self.id_marca) 

class Cliente(models.Model):
    rut              = models.CharField(primary_key=True, max_length=12, db_column = 'rut_cliente')
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    telefono         = models.CharField(max_length=9)
    email            = models.EmailField(unique=True, max_length=100)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)   


class Empleado(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10)
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    telefono         = models.CharField(max_length=9)
    email            = models.EmailField(unique=True, max_length=100)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)   

    
class Boleta(models.Model):
    id_boleta        = models.AutoField(primary_key=True    )
    fecha            = models.DateField(default=timezone.now)
    id_producto      = models.ForeignKey('Producto',on_delete=models.CASCADE, db_column = 'id_producto')
    precio_total     = models.CharField(max_length=6)

    def __str__(self):
        return str(self.id_boleta) + " " + str(self.fecha)