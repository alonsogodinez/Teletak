from django.conf.urls import patterns,  url

from .views import Index

urlpatterns = patterns('',

    url(r'^$', Index.as_view(),name='index'),
    # url(r'^add/$', RegisterMascota.as_view(),name='mascotas_add'),
    # url(r'^list/$', ListaMascota.as_view(),name='mascotas_list'),
    # url(r'^(?P<pk>\d+)/$', MascotaDetailView.as_view(),name='mascotas_detail'),
)