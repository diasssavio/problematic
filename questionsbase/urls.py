from django.conf.urls import patterns, url

urlpatterns = patterns('',
                       url(r'^(?P<id>\d+)/$', 'questionsbase.views.question'),

                       url(r'^course/$', 'questionsbase.views.listCourse'),
                       url(r'^theme/$', 'questionsbase.views.listTheme'),
                       url(r'^subjects/$', 'questionsbase.views.listSubjects'),

                       url(r'^search/(?P<choice>\w+)/(?P<word>\w+)/$', 'questionsbase.views.search'),

                       url(r'^logout/$', 'questionsbase.views.logout_view'),
)
