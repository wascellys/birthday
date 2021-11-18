import qrcode as qrcode
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from convite.models import Convite, Evento


def convite(request, codigo):
    convidado = Convite.objects.get(codigo=codigo)

    return render(request, 'convite/convite.html',{'convidado': convidado} )


def confirmar_presenca(request, codigo):
    convidado = Convite.objects.get(codigo=codigo)
    convidado.presente = True
    convidado.save()



    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def convidados(request, codigo):

    convidados = Convite.objects.filter(evento__codigo=codigo)
    return render(request, 'convite/convidados.html',{'convidados': convidados})


def eventos(request):
    eventos = Evento.objects.all().order_by('nome')
    return render(request, 'convite/eventos.html', {'eventos': eventos})

