from app.models import Producto


#Inicializa el carrito, lo guarda con su llave "carrito" relaionado a la sesion actual, de no existir carrito en la sesion lo crea y le da un diccionario.
class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito
#Indexa un objeto en el diccionario interno del carrito, si ya existe la key adentro, le suma valores a los ya existentes.
    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio": producto.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["precio"] += producto.precio
        self.guardar_carrito()

#Actualiza y guarda el carrito cuando se le llamae
    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True
#Elimina y guarda cambios
    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()
#Resta y guarda

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["precio"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()
#Vacia
    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True

 