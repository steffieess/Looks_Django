from django.shortcuts import render
from .models import Persona, Producto

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def hombre(request):
    return render(request,'core/hombre.html')

def mujer(request):
    return render(request,'core/mujer.html')

def Ayudanos(request):
    return render(request,'core/Ayudanos.html')

def contactanos(request):    
    return render(request,'core/contactanos.html')

def correorecu(request):
    return render(request,'core/correorecu.html')

def inicioSesion(request):
    return render(request,'core/inicioSesion.html')

def recuperarClave(request):
    return render(request,'core/recuperarClave.html')

def registro(request):
    return render(request,'core/registro.html')

def nosotros(request):
    return render(request,'core/nosotros.html')

def planhombre(request):
    return render(request,'core/planhombre.html')

def listarproductos (request):
    productos=Producto.objects.all()
    contexto = {"producto":productos}
    return render(request, 'core/listarproductos.html',contexto)

def lario(request):
    usuarios = Persona.objects.all() #trae todos los registros de la tabla (select*from)
    contexto = {"datos_user":usuarios}
    return render(request,'core/lario.html',contexto)


