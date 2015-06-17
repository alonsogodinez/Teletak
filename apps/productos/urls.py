from django.conf.urls import patterns,  url

from .views import Index

urlpatterns = patterns('',

    url(r'^$', Index.as_view(),name='index'),

)