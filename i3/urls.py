from django.conf.urls import url
from . import views

app_name = 'i3'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^wc/$', views.wc, name='wc'),
    url(r'^cockpit/$', views.cockpit, name='cockpit'),
    url(r'^engine/$', views.engine, name='engine'),
]