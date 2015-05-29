from django.conf.urls import patterns,  url

from .views import Configuracion, RegistrarTrabajador,ListarTrabajadores

urlpatterns = patterns('',

    url(r'^$', Configuracion.as_view(),name='index'),
    url(r'^nuevo/$', RegistrarTrabajador.as_view(),name='add_trabajador'),
    url(r'^list/$', ListarTrabajadores.as_view(),name='trabajadores_list'),
    # url(r'^(?P<pk>\d+)/$', MascotaDetailView.as_view(),name='mascotas_detail'),
)