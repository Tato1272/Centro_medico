from django.shortcuts import render, redirect, get_object_or_404
from .models import Hora
from .forms import HorasForm

# Create your views here.

def return_home(request):
    return render(request,"home.html")

def listar_hora(request):
    horas = Hora.objects.all()
    return render(request, "horas/listar_horas.html", {'horas': horas})

def add_hora(request):
    
    data={
        'form' : HorasForm()
    }
    
    if request.method == 'POST':
        formulario = HorasForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, "horas/add_hora.html", data)

def borrar_hora(request, id_hora):
    instancia = Hora.objects.get(id=id_hora)
    instancia.delete()
    return redirect('listar_horas')

def editar_hora(request, id_hora):
    hora = get_object_or_404(Hora, id=id_hora)
    
    data = {
        'form' : HorasForm(instance=hora)
    }
    
    if request.method == 'POST':
        formulario = HorasForm(data=request.POST, instance=hora, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect (to="listar_horas")
        data["form"] = formulario
    return render(request, "horas/editar_hora.html", data)