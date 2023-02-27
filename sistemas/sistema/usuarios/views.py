from django.shortcuts import render, redirect
#gabriel coloco esta libreria para trabajar html
from django.http import HttpResponse

from .models import Usuario

from .forms import UsuarioForm


# funcion a la que se le envia una solicitud y devuelve un texto html solo eso
def inicio(request):
    return render(request,'paginas/inicio.html');
    #return HttpResponse('<h2>Bienvenido Gabriel</h2>');
#accede a la carpeta templates al ser html pero necesita  el ruteo a paginas y renderiza

#'c:/Python/Python310/sistemas/sistema/usuarios/templates/paginas/nosotros.html')
#estaticas
def nosotros(request):
    return render(request,'paginas/nosotros.html');
def leer(request):
    return render(request,'paginas/leer.html');

#dinamicas
def usuario(request):
    #query = request.GET.get("buscar")
    #Usuarios = Usuario.objects.get(Nombres=query)
    Usuarios = Usuario.objects.all()
    print(Usuarios) 
    return render(request,'usuario/index.html',{'Usuarios': Usuarios})

def crear(request):
    formulario = UsuarioForm(request.POST or None,request.FILES or None)
    if formulario.is_valid(): 
        formulario.save()
        return redirect('usuario') 

     #return render(request,'usuario/crear.html')
    return render(request,'usuario/crear.html',{'formulario': formulario})

def editar(request, rowid):
    usuario = Usuario.objects.get(rowid=rowid)
    formulario = UsuarioForm(request.POST or None,request.FILES or None,instance=usuario)
    if formulario.is_valid() and request.POST: 
          formulario.save()
          return redirect('usuario') 
    return render(request,'usuario/editar.html',{'formulario': formulario})

def eliminar(request, rowid):
    usuario = Usuario.objects.get(rowid=rowid)
    usuario.delete()
    #return render(request,'usuario/editar.html');
    return redirect('usuario') 

def busqueda(request):
    query = request.GET.get("buscar")
    print (query)
    #Usuarios = Usuario.objects.get(Nombres=str(query))
    Usuarios = Usuario.objects.filter(Apellidos=query).values() | Usuario.objects.filter(Nombres=query).values()  | Usuario.objects.filter(id=query).values()
    #print(Usuarios) 
    return render(request,'usuario/busqueda.html',{'Usuarios': Usuarios})






# Create your views here.
