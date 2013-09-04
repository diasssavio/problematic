from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^$', 'questionsbase.views.index'),

                       url(r'^qb/', include('questionsbase.urls')),
                       # Examples:
                       # url(r'^$', 'problematic.views.home', name='home'),
                       # url(r'^problematic/', include('problematic.foo.urls')),

                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
)
