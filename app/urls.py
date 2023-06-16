from django.urls import path
from . import views


urlpatterns = [
    path('index', views.index, name = 'index'),
    path('about_us', views.about_us, name = 'about_us'),
    path('login', views.login, name = 'login'),
    path('registro', views.registro, name = 'registro'),
    path('error', views.error, name = 'error')

]