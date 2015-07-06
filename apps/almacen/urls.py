from django.conf.urls import patterns,  url, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api', SalidasViewSet)

urlpatterns = patterns('',

    url(r'^$', Index.as_view(),name='index'),
    url(r'^operaciones$', Operaciones.as_view(),name='operaciones'),
    url(r'^operaciones/ingresos$', IngresoMultiple.as_view(),name='ingresos'),
    url(r'^operaciones/reingresos$', Reingresos.as_view(),name='reingresos'),
    # url(r'^list/$', ListaMascota.as_view(),name='mascotas_list'),
    # url(r'^(?P<pk>\d+)/$', MascotaDetailView.as_view(),name='mascotas_detail'),
    url(r'^salidas$', Salidas.as_view(),name='salidas'),
#    url(r'^salidas/', include(router.urls)),
    url(r'^salidas/api/$', SalidasCollection.as_view()),
    url(r'^salidas/api/(?P<pk>\d+)/$', SalidasDelete.as_view())
)