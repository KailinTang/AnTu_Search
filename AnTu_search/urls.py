from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
                       # Examples:
                       #  url(r'^blog/', include('blog.urls')),
                       url(r'^search', 'antu.views.search'),
                       url(r'^submit', 'antu.views.submit'),
                       url(r'^info/(\d+)/$','antu.views.info',name='info')

                       # url(r'^admin/', include(admin.site.urls)),
                       )
