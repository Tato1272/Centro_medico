from django.shortcuts import render, redirect, get_object_or_404
from .models import Hora, Medico
from .forms import HorasForm

# Create your views here.


def return_home(request):
    return render(request, "home.html")


def listar_hora(request):
    horas = Hora.objects.all()
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
            data["mensaje"] = "guardado correctamente"
        else:
            data["form"] = formulario
    return render(request, "add_hora.html", data)


def borrar_hora(request, id_hora):
    instancia = Hora.objects.get(id=id_hora)
    instancia.delete()
    return redirect('listar_horas')


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
            return redirect(to="listar_hora")
        data["form"] = formulario
    return render(request, "editar_hora.html", data)
