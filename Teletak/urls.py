# -*- encoding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from apps.usuarios.views import Login,Logout
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "TELETAK"
admin.site.site_title= "Sistema de Administración"
# admin.site.index_title = "Bienvenido "

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', Login.as_view()),
    url(r'^logout/', Logout.as_view()),
    url(r'^',include('apps.almacen.urls', namespace='almacen')),
    url(r'^usuarios/',include('apps.usuarios.urls',namespace='usuarios')),
    url(r'^productos/',include('apps.productos.urls',namespace='productos')),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
