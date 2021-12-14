import json

import qrcode as qrcode
import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet



from convite.models import Convite, Evento




clients = {
    '123e4567-e89b-42d3-a456-426655440001':{'name': 'Edy', 'id': '3741088'}
}

url_base = "https://script.google.com/macros/s/AKfycbw31A1LB2x3ypGdWT90gRQQbJIPHdcu3Aib3g99sNVxvo-h4CDS-ZBswqN6u7e1-kReig/exec"


def convite(request, codigo):
    convidado = Convite.objects.get(codigo=codigo)

    return render(request, 'convite/convite.html', {'convidado': convidado})


def confirmar_presenca(request, codigo):
    convidado = Convite.objects.get(codigo=codigo)
    convidado.presente = True
    # convidado.save()

    convidado.confirmou_presenca()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def convidados(request, codigo):
    convidados = Convite.objects.filter(evento__codigo=codigo).order_by('pessoa')
    presentes = Convite.objects.filter(evento__codigo=codigo, presente=True).count()
    ausentes = Convite.objects.filter(evento__codigo=codigo, presente=False).count()
    return render(request, 'convite/convidados.html',
                  {'convidados': convidados, 'presentes': presentes, 'ausentes': ausentes})


def eventos(request):
    eventos = Evento.objects.all().order_by('nome')
    return render(request, 'convite/eventos.html', {'eventos': eventos})


def gerar_qrcode(request, codigo):
    convidados = Convite.objects.filter(evento__codigo=codigo)
    return render(request, 'qrcode.html', {'pessoas': convidados})





class GetSheetData(ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def token(self, request):

        if request.auth.key == request.data.get('api_key'):
            return Response(data={"message": "success"})
        else:
            return Response(data={"message": "invalid key"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        request = {
            "id_staff": "3741088",
            "api_key": request.auth,
        }
        try:
            response = requests.get(url=url_base, params=request)
            return Response(json.loads(response.content.decode('utf-8')))
        except AttributeError as error:
            raise error

