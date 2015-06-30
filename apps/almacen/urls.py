from django.conf.urls import patterns,  url

from .views import *

urlpatterns = patterns('',

    url(r'^$', Index.as_view(),name='index'),
    url(r'^operaciones$', Operaciones.as_view(),name='operaciones'),
    url(r'^operaciones/ingresos$', IngresoMultiple.as_view(),name='ingresos'),
    url(r'^operaciones/salidas$', Salidas.as_view(),name='salidas'),
    url(r'^operaciones/reingresos$', Reingresos.as_view(),name='reingresos'),
    # url(r'^list/$', ListaMascota.as_view(),name='mascotas_list'),
    # url(r'^(?P<pk>\d+)/$', MascotaDetailView.as_view(),name='mascotas_detail'),
)