from django.conf.urls import patterns,  url

from .views import Configuracion, RegistrarTrabajador

urlpatterns = patterns('',

    url(r'^$', Configuracion.as_view(),name='index'),
    url(r'^nuevo/$', RegistrarTrabajador.as_view(),name='add_user'),
    # url(r'^list/$', ListaMascota.as_view(),name='mascotas_list'),
    # url(r'^(?P<pk>\d+)/$', MascotaDetailView.as_view(),name='mascotas_detail'),
)