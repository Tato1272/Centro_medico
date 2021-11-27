from django.shortcuts import render, redirect, get_object_or_404
from .models import Hora, Medico
from .forms import HorasForm
from django.contrib import messages

# Create your views here.


def return_home(request):
    return render(request, "home.html")


def listar_hora(request,id_medico):
    horas = Hora.objects.filter(medico = id_medico)
    medicos = Medico.objects.all()
    data = {
        'horas': horas,
        'medicos': medicos
    }
    return render(request, "listar_horas.html", data)


def add_hora(request):

    medicos = Medico.objects.all()

    data = {
        'form': HorasForm(),
        'medicos': medicos
    }

    if request.method == 'POST':
        formulario = HorasForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Hora agregada correctamente')
            return redirect('listar_hora')
        else:
            data["form"] = formulario
    return render(request, "add_hora.html", data)


def borrar_hora(request, id_hora):
    instancia = Hora.objects.get(id=id_hora)
    instancia.delete()
    messages.success(request, 'Hora Eliminada Correctamente')
    return redirect('listar_hora')


def editar_hora(request, id_hora):
    hora = get_object_or_404(Hora, id=id_hora)

    data = {
        'form': HorasForm(instance=hora)
    }

    if request.method == 'POST':
        formulario = HorasForm(
            data=request.POST, instance=hora, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Hora Editada Correctamente')
            return redirect(to="listar_hora")
        data["form"] = formulario
    return render(request, "editar_hora.html", data)

def lista_medico(request):
    medicos = Medico.objects.all()
    return render(request, "lista_medico.html", {'medicos':medicos})