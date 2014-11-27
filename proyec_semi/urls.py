from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'proyec_semi.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('proyec_semi.apps.principal.urls')),
    url(r'^', include('proyec_semi.apps.usuarios.urls')),
)
