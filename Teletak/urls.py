# -*- encoding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from apps.usuarios.views import Login,Logout


admin.site.site_header = "Veterinaria HappyPets"
admin.site.site_title= "Sistema de Administración HappyPets "
admin.site.index_title = "Bienvenido 'user'"

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', Login.as_view()),
    url(r'^logout/', Logout.as_view()),
    url(r'^',include('apps.almacen.urls',namespace='almacen')),
    url(r'^usuarios/',include('apps.usuarios.urls',namespace='usuarios'))

]
