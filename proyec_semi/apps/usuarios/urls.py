from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^user/registro/$',registro_view),
)
