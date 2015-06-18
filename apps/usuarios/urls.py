from django.conf.urls import patterns,  url

from .views import Configuracion, RegistrarTrabajador,ListarTrabajadores,EditarTrabajador,EliminarTrabajador

urlpatterns = patterns('',

    url(r'^$', Configuracion.as_view(),name='index'),
    url(r'^nuevo/$', RegistrarTrabajador.as_view(),name='add_trabajador'),
    url(r'^lista/$', ListarTrabajadores.as_view(),name='trabajadores_list'),
    url(r'^editar/(?P<pk>\d+)/$', EditarTrabajador.as_view(),name='trabajador_detail'),
    url(r'^eliminar/(?P<pk>\d+)/$', EliminarTrabajador.as_view(),name='trabajador_delete'),
)
