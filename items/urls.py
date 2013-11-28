from django.conf.urls import patterns, url

from items import views

urlpatterns = patterns('',
     url(r'^$', views.index, name='index'),
     url(r'^(?P<item_id>\d+)/$', views.detail, name='detail'),
     url(r'^item_type/(?P<item_type_id>\d+)/$', views.item_type_detail, 
        name='item_type_detail'),
)
