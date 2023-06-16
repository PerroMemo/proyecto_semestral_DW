from django.db import models

# Create your models here.


class Marca(models.Model):
    id_marca        = models.AutoField(db_column='idMarca', primary_key=True)  
    nombre           = models.CharField(max_length=20)

    def __str__(self):
        return str(self.nombre)

class Producto(models.Model):
    id              = models.CharField(primary_key=True, max_length=4)
    nombre           = models.CharField(max_length=20)
    marca            = models.CharField(max_length=20)
    precio         = models.IntegerField(max_length=6)
    id_marca        = models.ForeignKey('Marca',on_delete=models.CASCADE, db_column='idMarca')  
    stock           = models.CharField(max_length=4)

    def __str__(self):
        return str(self.nombre)+" "+str(self.marca)

class Cliente(models.Model):
    rut              = models.CharField(primary_key=True, max_length=10, db_column = 'rut_cliente')
    nombre           = models.CharField(max_length=20)
    apellido_paterno = models.CharField(max_length=20)
    apellido_materno = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False) 
    telefono         = models.IntegerField(max_length=8)
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
    telefono         = models.IntegerField(max_length=45)
    email            = models.EmailField(unique=True, max_length=100)
    direccion        = models.CharField(max_length=50, blank=True, null=True)  

    def __str__(self):
        return str(self.nombre)+" "+str(self.apellido_paterno)   

    
class Boleta(models.Model):
    id_boleta        = models.CharField(primary_key=True, max_length=4)
    rut_cliente      = models.ForeignKey('Cliente',on_delete=models.CASCADE, db_column = 'rut_cliente')
    nombre_producto  = models.CharField(max_length=20)
    email            = models.EmailField(unique=True, max_length=100, blank= False)
    precio_total     = models.CharField(max_length=6)

    def __str__(self):
        return str(self.rut_cliente) + " " +  str(self.nombre_producto)

