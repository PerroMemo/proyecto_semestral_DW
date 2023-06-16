from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Cliente, Marca, Producto, Empleado, Ticket

from .forms import ClientesForm, MarcaForm, TicketForm, EmpleadosForm, ProductoForm
# Create your views here.

def index(request):

    context = {}
    return render(request, 'app/index.html',context)


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
        context={'clientes': clientes, 'mensajes': mensajes, 'errores': errores}
        return render(request,"app/clientes_list.html",context)
    
def clientes_edit(request, pk):
    try:
        cliente=Cliente.objects.get(rut=pk)
        context={}
        if clientes:
            print("Edit encontró el cliente...")
            form=ClientesForm(request.POST,instance=cliente)
            form.save()
            mensaje="Bien, datos actualizados..."
            print(mensaje)
            context={'cliente': cliente, 'form': form, 'mensaje': mensaje}
            return render(request,"app/clientes_edit.html",context)
    except:
        print("Error, rut no existe...")
        clientes=Cliente.objects.all()
        mensaje="Error, rut no existe"
        context={'mensaje': mensaje, 'clientes': clientes}
        return render(request,"app/clientes_list.html",context)
    
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
            form=MarcaForm(request.POST,instance=marca)
            form.save()
            mensaje="Bien, datos actualizados..."
            print(mensaje)
            context={'marca': marca, 'form': form, 'mensaje': mensaje}
            return render(request,"app/marcas_edit.html",context)
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
    context={}

    if request.method == "POST":
        print("controlador es un post...")
        form = ProductoForm(request.POST)
        if form.is_valid:
            print("estoy en agregar, is_valid")
            form.save()

            #limpiar form
            form=ProductoForm()

            context={'mensaje':"Ok, datos grabados...","form":form}
            return render(request,"app/productos_add.html",context)
    else:
        form = ProductoForm()
        context={'form':form}
        return render(request,"app/productos_add.html",context)
    
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
            form=ProductoForm(request.POST,instance=producto)
            form.save()
            mensaje="Bien, datos actualizados..."
            print(mensaje)
            context={'producto': producto, 'form': form, 'mensaje': mensaje}
            return render(request,"app/productos_edit.html",context)
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
            form=EmpleadosForm(request.POST,instance=empleado)
            form.save()
            mensaje="Bien, datos actualizados..."
            print(mensaje)
            context={'empleado': empleado, 'form': form, 'mensaje': mensaje}
            return render(request,"app/empleados_edit.html",context)
    except:
        print("Error, rut no existe...")
        empleados=Empleado.objects.all()
        mensaje="Error, rut no existe"
        context={'mensaje': mensaje, 'empleados': empleados}
        return render(request,"app/empleados_list.html",context)
    
def crud_ticket(request):

    tickets=Ticket.objects.all()
    context={'tickets':tickets}
    print("enviando datos tickets_list")
    return render(request,"alumnos/tickets_list.html",context)

def ticketAdd(request):
    print("estoy en controlador ticketAdd...")
    context={}

    if request.method == "POST":
        print("controlador es un post...")
        form = TicketForm(request.POST)
        if form.is_valid:
            print("estoy en agregar, is_valid")
            form.save()

            #limpiar form
            form=TicketForm()

            context={'mensaje':"Ok, datos grabados...","form":form}
            return render(request,"alumnos/tickets_add.html",context)
    else:
        form = TicketForm()
        context={'form':form}
        return render(request,"alumnos/tickets_add.html",context)
    
def ticket_del(request, pk):
    mensajes=[]
    errores=[]
    tickets= Ticket.objects.all()
    try:
        ticket=Ticket.objects.get(rut_cliente=pk)
        context={}
        if ticket:
            ticket.delete()
            mensaje.append("Bien, datos eliminados...")
            context={'tickets': tickets, 'mensajes': mensajes, 'errores': errores}
            return render(request,"alumnos/tickets_list.html",context)
    except:
        print("Error, rut_cliente no existe...")
        tickets=Ticket.objects.all()
        mensaje="Error, rut_cliente no existe"
        context={'tickets': tickets, 'mensajes': mensajes, 'errores': errores}
        return render(request,"alumnos/tickets_list.html",context)
    
def ticket_edit(request, pk):
    try:
        ticket=Ticket.objects.get(rut_cliente=pk)
        context={}
        if ticket:
            print("Edit encontró el ticket...")
            form=TicketForm(request.POST,instance=ticket)
            form.save()
            mensaje="Bien, datos actualizados..."
            print(mensaje)
            context={'ticket': ticket, 'form': form, 'mensaje': mensaje}
            return render(request,"alumnos/tickets_edit.html",context)
    except:
        print("Error, rut_cliente no existe...")
        tickets=Ticket.objects.all()
        mensaje="Error, rut_cliente no existe"
        context={'mensaje': mensaje, 'tickets': tickets}
        return render(request,"alumnos/tickets_list.html",context)