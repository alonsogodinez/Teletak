from django.conf.urls import patterns,  url
from .views import Index,ListarProductos,EliminarProducto,RegistrarProducto,EditarProducto

urlpatterns = patterns('',

    url(r'^$', Index.as_view(),name='index'),
    url(r'^listar$', ListarProductos.as_view(),name='Listar_Productos'),
    url(r'^eliminar/(?P<pk>\d+)/$', EliminarProducto.as_view(),name='Eliminar_Producto'),
    url(r'^registrar$',RegistrarProducto.as_view(),name='Registrar_Producto'),
    url(r'^editar/(?P<pk>\d+)/$',EditarProducto.as_view(),name='Editar_Producto'),
)