from django.forms import modelform_factory
from django.shortcuts import render, redirect
from django.http import HttpResponse


# Create your views here.
from webapp.forms import PersonaForm
from webapp.models import *


def bienvenido(request):
    nro_persona = Persona.objects.count()
    persona = Persona.objects.all()
    return render(request, 'bienvenido.html',{'nro': nro_persona, 'personas': persona})





def detallePersona(request, id):
    persona = Persona.objects.get(pk=id)
    return render(request, 'detalle.html', {'persona': persona})



#PersoForm = modelform_factory(Persona, exclude=[])

def nuevaPersona(request):
    if request.method == 'POST':
        formaPersona = PersonaForm(request.POST)
        if formaPersona.is_valid():
            formaPersona.save()
            return redirect('index')
    else:
        formaPersona = PersonaForm

    return render(request, 'nuevo.html', {'formaPersona': formaPersona})






"""def despedida(request):
    return HttpResponse('Despedida desde Django')

def contacto(request):
    return HttpResponse('Email: contacto@mail.com, Tel. 5544332211')"""