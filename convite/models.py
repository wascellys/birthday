import qrcode
from django.db import models

# Create your models here.
from django.db import models
from django.utils.crypto import get_random_string
# Create your models here.
from eventos import settings


def create_if_hash():
    return get_random_string(10)
    if not Evento.objects.filter(codigo=hash).exists():
        return hash
    else:
        return create_if_hash()

class Evento(models.Model):
    codigo = models.CharField(max_length=10, default=create_if_hash, unique=True, null=True, blank=True)
    nome = models.CharField(max_length=255, blank=True, null=True)
    data = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return str(self.nome)

class Convite(models.Model):
    codigo = models.CharField(max_length=10, default=create_if_hash, unique=True, null=True, blank=True)
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)
    pessoa = models.CharField(max_length=255, blank=True, null=True)
    presente = models.BooleanField(default=False)


    def __str__(self):
        return str(self.pessoa)+ " - " +str(self.evento)


    def qrcode(self):
        import socket

        hostname = socket.gethostname()
        ip = socket.gethostbyname(hostname)
        print(hostname)
        qr = qrcode.QRCode(
            version=1,
            box_size=15,
            border=4
        )

        codigo = self.codigo

        # data = 'http://' + ip + ":8000/convite/"+codigo

        data = 'https://edywascellys.pythonanywhere.com/convite/'+codigo


        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color='white', back_color='#5FBF00')
        img.save('/home/edywascellys/edywascellys.pythonanywhere.com/static/img/'+codigo+'.png')

        # img.save('../birthday/convite/static/img/' + codigo + '.png')
        imagem = '/static/img/'+codigo+'.png'

        return imagem