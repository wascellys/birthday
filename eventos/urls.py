"""eventos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from convite.views import convite, confirmar_presenca, eventos, convidados, gerar_qrcode, GetSheetData
from eventos import settings

get_sheet_data = GetSheetData.as_view({"get": "get"})
token = GetSheetData.as_view({"post": "token"})


urlpatterns = [
    path('admin/', admin.site.urls),
    path('convite/<str:codigo>', convite, name="convite"),
    path('confirmar-presenca/<str:codigo>', confirmar_presenca, name="confirmar-presenca"),
    path('convidados/<str:codigo>', convidados, name="confirmar-presenca"),
    path('gerar_qrcode/<str:codigo>', gerar_qrcode, name="gerar_qrcode"),
    path('', eventos, name="eventos"),
    path('api-auth/', include('rest_framework.urls')),
    path("sheet/", get_sheet_data, name="get_data"),
    path("token/", token, name="token"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
