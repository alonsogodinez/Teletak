from django.conf.urls import patterns,  url, include
from .views import *


urlpatterns = patterns('',

    url(r'^$', Index.as_view(),name='index'),
    url(r'^operaciones$', Operaciones.as_view(),name='operaciones'),
    url(r'^operaciones/ingresos$', IngresoMultiple.as_view(),name='ingresos'),
    url(r'^operaciones/reingresos$', Reingresos.as_view(),name='reingresos'),
    url(r'^operaciones/salidas$',SalidaView.as_view(), name='salidas'),
    url(r'^operaciones/listar_salidas$',ListarSalidas.as_view(), name='lista_salidas'),
    url(r'^operaciones/eliminar_salidas/(?P<pk>\d+)/$',EliminarSalida.as_view(), name='eliminar_salidas'),
    url(r'^operaciones/almacen/(\d+)/$','apps.almacen.views.prueba',name="prueba"),
   # url(r'^prueba/(\d+)/$','apps.almacen.views.prueba', name='prueba'),
)