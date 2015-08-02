from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<department_id>[0-9]+)/$', views.index2, name='index2'),
    url(r'^(?P<department_id>[0-9]+)/Advisor/(?P<advisor_id>[0-9]+)/$' , views.advisorinfo, name= 'advisorinfo'),
    url(r'^(?P<department_id>[0-9]+)/Advisor/(?P<advisor_id>[0-9]+)/Students/$', views.detail, name='detail'),
    url(r'^(?P<department_id>[0-9]+)/Advisor/(?P<advisor_id>[0-9]+)/Degrees/$', views.advisordegree, name='advisordegree'),
    # ex: /polls/5/results/
    url(r'^(?P<department_id>[0-9]+)/Degree/(?P<degree_id>[0-9]+)/$', views.degree, name='degree'),
    url(r'^(?P<department_id>[0-9]+)/Certificate/(?P<certificate_id>[0-9]+)/$', views.certificate, name='certificate'),
    # ex: /polls/5/vote/
    url(r'^Degree/(?P<degree_id>[0-9]+)/Courses/(?P<degree_core_course_structure_id>[0-9]+)/$', views.coursedegree, name='coursedegree'),
]