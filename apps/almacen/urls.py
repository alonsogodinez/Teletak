from django.conf.urls import patterns,  url, include
from .views import *


urlpatterns = patterns('',

    url(r'^$', Index.as_view(),name='index'),
    url(r'^operaciones$', Operaciones.as_view(),name='operaciones'),
    url(r'^operaciones/ingresos$', IngresoMultiple.as_view(),name='ingresos'),
    url(r'^operaciones/reingresos$', Reingresos.as_view(),name='reingresos'),
    url(r'^operaciones/salidas',SalidaView.as_view(), name='salidas'),
    url(r'^operaciones/registrar_salida','apps.almacen.views.RegistrarSalida', name='Registrar_Salida'),
    url(r'^operaciones/add_detalle_salida','apps.almacen.views.AddDetalleSalida', name='Add_Detalle_Salida'),

)