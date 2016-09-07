from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^P(?P<question_id>[0-9]+)/$', views.detail,name='details'),
    url(r'^P(?P<question_id>[0-9]+)/result/$', views.result, name='result'),
    url(r'^P(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote')
]