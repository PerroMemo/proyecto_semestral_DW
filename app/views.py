from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

#Compra
from app.Carrito import Carrito
from django.utils import timezone
from datetime import datetime
from app.models import Cliente, Marca, Producto, Empleado, Boleta
from .forms import ClientesForm, MarcaForm, BoletaForm, EmpleadosForm, ProductoForm, RegistroForm
# Create your views here.

def index(request):

    context = {}
    productos = Producto.objects.all()
    return render(request, 'app/index.html',{'productos': productos})


def about_us(request):

    context = {}
    return render(request, 'app/about_us.html',context)

def login(request):

    context = {}
    return render(request, 'app/login.html',context)

def registro(request):

    context = {}
    return render(request, 'app/registro.html',context)

def error(request):

    context = {}
    return render(request, 'app/error.html',context)

def comprar(request):

    context = {}
    return render(request, 'app/comprar.html',context)

def crudhub(request):

    context = {}
    return render(request, 'app/crudhub.html',context)

def crud_clientes(request):

    clientes=Cliente.objects.all()
    context={'clientes':clientes}
    print("enviando datos clientes_list")
    return render(request,"app/clientes_list.html",context)

def clientesAdd(request):
    print("estoy en controlador clientesAdd...")
    context={}

    if request.method == "POST":
        print("controlador es un post...")
        form = ClientesForm(request.POST)
        if form.is_valid:
            print("estoy en agregar, is_valid")
            form.save()

            #limpiar form
            form=ClientesForm()

            context={'mensaje':"Ok, datos grabados...","form":form}
            return render(request,"app/clientes_add.html",context)
    else:
        form = ClientesForm()
        context={'form':form}
        return render(request,"app/clientes_add.html",context)


#Este DEL funciona 
def clientes_del(request, pk):
    mensajes=[]
    errores=[]
    clientes= Cliente.objects.all()
    try:
        cliente=Cliente.objects.get(rut=pk)
        
        context={}
        if cliente:
            cliente.delete()
            mensaje.append("Bien, datos eliminados...")
            context={'clientes': clientes, 'mensajes': mensajes, 'errores': errores}
            return render(request,"app/clientes_list.html",context)
    except:
        print("Error, id no existe...")
        clientes=Cliente.objects.all()
        mensaje="Error, rut no existe"
        context={'clientes': clientes, 'mensajes': mensajes}
        return render(request,"app/clientes_list.html",context)
    

#USAR ESTE COMO BASE PARA EL RESTO DE EDITS
def clientes_edit(request, pk):
    try:
        #error en la tomada de pk
        cliente = Cliente.objects.get(rut=pk)
        print(cliente)

        context = {}
       
        if cliente:
            print("Edit encontró el cliente...")
            if request.method == "POST":
                print("Es POST")
                form = ClientesForm(request.POST, instance=cliente)
                if form.is_valid():
                    form.save()
                    mensaje = "Bien, datos actualizados..."
                    print(mensaje)
                    context = {'cliente': cliente, 'form': form, 'mensaje': mensaje}
                    return render(request, "app/clientes_edit.html", context)
            else:
                print("No es POST")
                form = ClientesForm(instance=cliente)
                mensaje = ""
                context = {'cliente': cliente, 'form': form, 'mensaje': mensaje}
                return render(request, "app/clientes_edit.html", context)
   
    except:
        print("Error, rut no existe...")
        clientes = Cliente.objects.all()
        mensaje = "Error, rut no existe"
        context = {'mensaje': mensaje, 'clientes': clientes}
        return render(request, "app/clientes_list.html", context)
    
def crud_marca(request):

    marcas=Marca.objects.all()
    context={'marcas':marcas}
    print("enviando datos marcas_list")
    return render(request,"app/marcas_list.html",context)

def marcaAdd(request):
    print("estoy en controlador marcasAdd...")
    context={}

    if request.method == "POST":
        print("controlador es un post...")
        form = MarcaForm(request.POST)
        if form.is_valid:
            print("estoy en agregar, is_valid")
            form.save()

            #limpiar form
            form=MarcaForm()

            context={'mensaje':"Ok, datos grabados...","form":form}
            return render(request,"app/marcas_add.html",context)
    else:
        form = MarcaForm()
        context={'form':form}
        return render(request,"app/marcas_add.html",context)
    
def marca_del(request, pk):
    mensajes=[]
    errores=[]
    marcas= Marca.objects.all()
    try:
        marca=Marca.objects.get(id_marca=pk)
        context={}
        if marca:
            marca.delete()
            mensaje.append("Bien, datos eliminados...")
            context={'marcas': marcas, 'mensajes': mensajes, 'errores': errores}
            return render(request,"app/marcas_list.html",context)
    except:
        print("Error, id no existe...")
        marcas=Marca.objects.all()
        mensaje="Error, id no existe"
        context={'marcas': marcas, 'mensajes': mensajes, 'errores': errores}
        return render(request,"app/marcas_list.html",context)
    
def marca_edit(request, pk):
    try:
        marca=Marca.objects.get(id_marca=pk)
        context={}
        if marca:
            print("Edit encontró la marca...")
            if request.method == "POST":
                form=MarcaForm(request.POST,instance=marca)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context={'marca': marca, 'form': form, 'mensaje': mensaje}
                return render(request,"app/marcas_edit.html",context)
            else:
                print("edit, NO es un POST")
                form = MarcaForm(instance=marca)
                mensaje = ""
                context = {'marca': marca, 'form': form, 'mensaje': mensaje}
                return render(request, "app/marcas_edit.html", context)
    except:
        print("Error, id no existe...")
        marcas=Marca.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje': mensaje, 'marcas': marcas}
        return render(request,"app/marcas_list.html",context)
    
def crud_productos(request):

    productos=Producto.objects.all()
    context={'productos':productos}
    print("enviando datos productos_list")
    return render(request,"app/productos_list.html",context)

def productosAdd(request):
    print("estoy en controlador productosAdd...")
    context = {}

    if request.method == "POST":
        print("controlador es un post...")
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            print("estoy en agregar, is_valid")
            form.save()

            form = ProductoForm()  # Limpiar form

            context = {'mensaje': "Ok, datos grabados...", "form": form}
            return render(request, "app/productos_add.html", context)
        else:
            context = {'form': form}
            return render(request, "app/productos_add.html", context)  
    else:
        form = ProductoForm()
        context = {'form': form}
        return render(request, "app/productos_add.html", context)
    
def productos_del(request, pk):
    mensajes=[]
    errores=[]
    productos= Producto.objects.all()
    try:
        producto=Producto.objects.get(id=pk)
        context={}
        if producto:
            producto.delete()
            mensaje.append("Bien, datos eliminados...")
            context={'productos': productos, 'mensajes': mensajes, 'errores': errores}
            return render(request,"app/productos_list.html",context)
    except:
        print("Error, id no existe...")
        productos=Producto.objects.all()
        mensaje="Error, id no existe"
        context={'productos': productos, 'mensajes': mensajes, 'errores': errores}
        return render(request,"app/productos_list.html",context)
    
def productos_edit(request, pk):
    try:
        producto=Producto.objects.get(id=pk)
        context={}
        if producto:
            print("Edit encontró el producto...")
            if request.method == "POST":
                form=ProductoForm(request.POST,instance=producto)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context={'producto': producto, 'form': form, 'mensaje': mensaje}
                return render(request,"app/productos_edit.html",context)
            else:
                print("edit, NO es un POST")
                form = ProductoForm(instance=producto)
                mensaje = ""
                context = {'producto': producto, 'form': form, 'mensaje': mensaje}
                return render(request, "app/productos_edit.html", context)    
    except:
        print("Error, id no existe...")
        productos=Producto.objects.all()
        mensaje="Error, id no existe"
        context={'mensaje': mensaje, 'productos': productos}
        return render(request,"app/productos_list.html",context)
    
def crud_empleados(request):

    empleados=Empleado.objects.all()
    context={'empleados':empleados}
    print("enviando datos empleados_list")
    return render(request,"app/empleados_list.html",context)

def empleadosAdd(request):
    print("estoy en controlador empleadosAdd...")
    context={}

    if request.method == "POST":
        print("controlador es un post...")
        form = EmpleadosForm(request.POST)
        if form.is_valid:
            print("estoy en agregar, is_valid")
            form.save()

            #limpiar form
            form=EmpleadosForm()

            context={'mensaje':"Ok, datos grabados...","form":form}
            return render(request,"app/empleados_add.html",context)
    else:
        form = EmpleadosForm()
        context={'form':form}
        return render(request,"app/empleados_add.html",context)
    
def empleados_del(request, pk):
    mensajes=[]
    errores=[]
    empleados= Empleado.objects.all()
    try:
        empleado=Empleado.objects.get(rut=pk)
        context={}
        if empleado:
            empleado.delete()
            mensaje.append("Bien, datos eliminados...")
            context={'empleados': empleados, 'mensajes': mensajes, 'errores': errores}
            return render(request,"app/empleados_list.html",context)
    except:
        print("Error, rut no existe...")
        empleados=Empleado.objects.all()
        mensaje="Error, rut no existe"
        context={'empleados': empleados, 'mensajes': mensajes, 'errores': errores}
        return render(request,"app/empleados_list.html",context)
    
def empleados_edit(request, pk):
    try:
        empleado=Empleado.objects.get(rut=pk)
        context={}
        if empleado:
            print("Edit encontró el empleado...")
            if request.method == "POST":
                form=EmpleadosForm(request.POST,instance=empleado)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context={'empleado': empleado, 'form': form, 'mensaje': mensaje}
                return render(request,"app/empleados_edit.html",context)
            else:
                print("No es POST")
                form = EmpleadosForm(instance=empleado)
                mensaje = ""
                context = {'empleado': empleado, 'form': form, 'mensaje': mensaje}
                return render(request, "app/empleados_edit.html", context)
    except:
        print("Error, rut no existe...")
        empleados=Empleado.objects.all()
        mensaje="Error, rut no existe"
        context={'mensaje': mensaje, 'empleados': empleados}
        return render(request,"app/empleados_list.html",context)
    
def crud_boleta(request):

    boletas=Boleta.objects.all()
    context={'boletas':boletas}
    print("enviando datos boletas_list")
    return render(request,"app/boletas_list.html",context)

def boletaAdd(request):
    print("estoy en controlador boletaAdd...")
    context={}

    if request.method == "POST":
        print("controlador es un post...")
        form = BoletaForm(request.POST)
        if form.is_valid:
            print("estoy en agregar, is_valid")
            form.save()

            #limpiar form
            form=BoletaForm()

            context={'mensaje':"Ok, datos grabados...","form":form}
            return render(request,"app/boletas_add.html",context)
    else:
        form = BoletaForm()
        context={'form':form}
        return render(request,"app/boletas_add.html",context)
    
def boleta_del(request, pk):
    mensajes=[]
    errores=[]
    boletas= Boleta.objects.all()
    try:
        boleta=Boleta.objects.get(id_boleta=pk)
        context={}
        if boleta:
            boleta.delete()
            mensaje.append("Bien, datos eliminados...")
            context={'boletas': boletas, 'mensajes': mensajes, 'errores': errores}
            return render(request,"app/boletas_list.html",context)
    except:
        print("Error, id_boleta no existe...")
        boletas=Boleta.objects.all()
        mensaje="Error, id_boleta no existe"
        context={'boletas': boletas, 'mensajes': mensajes, 'errores': errores}
        return render(request,"app/boletas_list.html",context)
    
def boleta_edit(request, pk):
    try:
        boleta=Boleta.objects.get(id_boleta=pk)
        print(boleta)

        context={}
        if boleta:
            print("Edit encontró la boleta...")
            if request.method == "POST":
                print("edit, es un POST")
                form=BoletaForm(request.POST,instance=boleta)
                form.save()
                mensaje="Bien, datos actualizados..."
                print(mensaje)
                context={'boleta': boleta, 'form': form, 'mensaje': mensaje}
                return render(request,"app/boletas_edit.html",context)
            else:
                print("edit, NO es un POST")
                form = BoletaForm(instance=boleta)
                mensaje = ""
                context = {'boleta': boleta, 'form': form, 'mensaje': mensaje}
                return render(request,"app/boletas_edit.html", context)
    except:
        print("Error, id_boleta no existe...")
        boletas=Boleta.objects.all()
        mensaje="Error, id_boleta no existe"
        context={'mensaje': mensaje, 'boletas': boletas}
        return render(request,"app/boletas_list.html",context)
    
def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registro') 
    else:
        form = RegistroForm()
    
    return render(request, 'app/registro.html', {'form': form})

#COMPRAS


def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("index")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("index")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("index")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("index")


#Funcional~
#Cambia stock e inserta boletas. 
#Errores conocidos, no puede guardar los ids de cada producto



def restarStock_producto(request):
    carrito = Carrito(request)
    set_carro =  request.session["carrito"].items()
    print(set_carro)
    precio_total_prod = 0
    ls_productos = []
    producto = None
    for i in set_carro:
        tuplex = i[1]

        id_buscar = tuplex["producto_id"]
        resto = tuplex["cantidad"]
        precio_total_prod = precio_total_prod + tuplex["precio"]
        
        
        producto = Producto.objects.get(id=id_buscar)        

        ls_productos.append(producto)

        print(producto)
        print( producto.stock)

        producto.stock =  int(producto.stock) - resto
        print( producto.stock)
        producto.save()
    
    print(precio_total_prod)
    print(ls_productos)
    fecha_str = datetime.now().date().isoformat()
    #No deja comprar con el carro vacio
    try:
        if producto == None:
            raise Producto.DoesNotExist

    except Producto.DoesNotExist:
        print("No existe")
        return redirect("error")

    nueva_boleta = Boleta(fecha= fecha_str, id_producto = producto , precio_total = precio_total_prod)

    nueva_boleta.save()
    carrito.limpiar()
    return redirect("index")

