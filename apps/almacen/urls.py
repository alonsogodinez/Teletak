from django.conf.urls import patterns,  url, include
from .views import *


urlpatterns = patterns('',

    url(r'^$', Index.as_view(),name='index'),
    url(r'^operaciones$', Operaciones.as_view(),name='operaciones'),
    url(r'^operaciones/ingresos$', IngresoView.as_view(),name='ingresos'),
    url(r'^operaciones/reingresos$', Reingresos.as_view(),name='reingresos'),
    url(r'^operaciones/salidas$',SalidaView.as_view(), name='salidas'),

    url(r'^operaciones/listar_ingresos/$',ListarIngresos.as_view(), name='lista_ingresos'),
    url(r'^operaciones/listar_ingresos/(\d+)/$',DetalleIngresoView.as_view(), name='detalle_ingresos'),


    url(r'^operaciones/listar_reingresos$',ListarReingresoView.as_view(), name='lista_reingreso'),
    url(r'^operaciones/listar_reingresos/(\d+)/$$',DetalleReingresoView.as_view(), name='detalle_reingreso'),

    url(r'^operaciones/listar_salidas$',ListarSalidas.as_view(), name='lista_salidas'),
    url(r'^operaciones/listar_salidas/(\d+)/$',DetalleSalidaView.as_view(), name='detalle_salidas'),

    url(r'^operaciones/getproducto/$','apps.almacen.views.getProductosfromAlmacen',name="getProductosfromAlmacen"),
    url(r'^operaciones/getcantidad/(\d+)/(\d+)/$','apps.almacen.views.getCantidadfromProductos',name="getCantidadfromProductos"),
    url(r'^reporte', Reporte.as_view(),name='reporte'),
)