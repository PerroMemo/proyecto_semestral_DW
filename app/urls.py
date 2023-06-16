from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name = 'index'),
    path('about_us', views.about_us, name = 'about_us'),
    path('login', views.login, name = 'login'),
    path('registro', views.registro, name = 'registro'),
    path('error', views.error, name = 'error'),
    path('crud_clientes', views.crud_clientes, name = 'crud_clientes'),
    path('clientesAdd', views.clientesAdd, name='clientesAdd'),
    path('clientes_del/<str:pk>', views.clientes_del, name='clientes_del'),
    path('clientes_edit/<str:pk>', views.clientes_edit, name='clientes_edit'),
    path('crud_marca', views.crud_marca, name = 'crud_marca'),
    path('marcaAdd', views.marcaAdd, name='marcaAdd'),
    path('marca_del/<str:pk>', views.marca_del, name='marca_del'),
    path('marca_edit/<str:pk>', views.marca_edit, name='marca_edit'),
    path('crud_productos', views.crud_productos, name = 'crud_productos'),
    path('productosAdd', views.productosAdd, name='productosAdd'),
    path('productos_del/<str:pk>', views.productos_del, name='productos_del'),
    path('productos_edit/<str:pk>', views.productos_edit, name='productos_edit'),
    path('crud_empleados', views.crud_empleados, name = 'crud_empleados'),
    path('empleadosAdd', views.empleadosAdd, name='empleadosAdd'),
    path('empleados_del/<str:pk>', views.empleados_del, name='empleados_del'),
    path('empleados_edit/<str:pk>', views.empleados_edit, name='empleados_edit'),
    path('crud_ticket', views.crud_ticket, name = 'crud_ticket'),
    path('ticketAdd', views.ticketAdd, name='ticketAdd'),
    path('ticket_del/<str:pk>', views.ticket_del, name='ticket_del'),
    path('ticket_edit/<str:pk>', views.ticket_edit, name='ticket_edit'),
    
]