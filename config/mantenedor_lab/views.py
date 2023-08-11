from django.shortcuts import get_object_or_404, render
from .form import CrearFormularioLab
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *
# Create your views here.

def index(request):
    lista_lab = Laboratorio.objects.filter()
    return render(request, 'index.html', {'lista_lab': lista_lab,'error': ""})


def editar(request,edit_id ):
    if request.method == 'GET':
            print("get")
            buscar_obj = get_object_or_404(Laboratorio,pk=edit_id)
            formulario = CrearFormularioLab(instance=buscar_obj)
            return render(request, 'detalle.html', {'lista':buscar_obj, 'formulario':formulario,'error': ""}) 
    else:           
        try:
            print("post")
            buscar_obj = get_object_or_404(Laboratorio,pk=edit_id)
            editar_lab = CrearFormularioLab(request.POST, instance=buscar_obj)
            editar_lab.save()
            lista_lab = Laboratorio.objects.filter()
            return render(request, 'index.html', {'lista_lab': lista_lab,'error': "Editado Correctamente"})
        except ValueError:
            print("error")
            lista_lab = Laboratorio.objects.filter()
            modelo_html =lista_lab.model.__name__
            return render(request, 'index.html', {'lista_lab': lista_lab,'error': "Error al Guardar"})



def ingresar(request):
    if request.method == 'GET':
        return render(request, 'ingresar.html', {'form':  CrearFormularioLab})
    else:
        try:
            form = CrearFormularioLab(request.POST)
            nuevo_lab = form.save(commit=False)
            # nueva_vehiculo.usuario = request.user
            nuevo_lab.save()
            return render(request, 'ingresar.html', {'form': CrearFormularioLab, 'error': 'Laboratorio Ingresado correctamente'})
        except ValueError:
            return render(request, 'ingresar.html', {'form': CrearFormularioLab, 'error': 'Datos erroneos'})

    
def eliminar(request, lab_id): 
    if request.method == 'GET':
        lab_buscar = get_object_or_404(Laboratorio,pk=lab_id)
        formulario = CrearFormularioLab(instance=lab_buscar)
        return render(request, 'eliminar.html', {'lista': lab_buscar, 'formulario':formulario})      
    else:           
        try:
            lab_buscar = get_object_or_404(Laboratorio,pk=lab_id)
            lab_buscar.delete()
            lista_lab = Laboratorio.objects.filter()
            return render(request, 'index.html', {'lista_lab': lista_lab,'error': "Eliminado Correctamente"})
        except ValueError:
            return render(request, 'index.html', {'lista_v': lista_lab, 'error': "Error Eliminacin"})