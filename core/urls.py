from django.contrib import admin
from django.urls import path, include
from .views import home, Ayudanos, contactanos, correorecu, hombre, listarproductos, mujer, nosotros, inicioSesion, recuperarClave, registro, lario, planhombre

urlpatterns = [
    path('home', home, name="home"),
    path('hombre', hombre, name="hombre"),
    path('mujer', mujer, name="mujer"),
    path('ayudanos', Ayudanos, name="ayudanos"),
    path('contactanos', contactanos, name="contactanos"),
    path('registro', registro, name="registro"),
    path('recuperarclave', recuperarClave, name="recuperarclave"),
    path('correorecu', correorecu, name="correorecu"),
    path('nosotros', nosotros, name="nosotros"),
    path('iniciosesion', inicioSesion, name="iniciosesion"),
    path('listarproductos', listarproductos, name="listarproductos"),
    path('formulario', lario, name="formulario"),
    path('planhombre', planhombre, name="planhombre")

    
]
