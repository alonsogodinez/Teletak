
from django.conf.urls import include, url
from django.contrib import admin
from apps.users.views import Login,Logout



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', Login.as_view()),
    url(r'^logout/', Logout.as_view()),
    url(r'^',include('apps.almacen.urls',namespace='almacen')),

]
