from django.conf.urls import patterns, url

from items import views

urlpatterns = patterns('',
     url(r'^$', views.index, name='index'),
     url(r'^(?P<item_id>\d+)/$', views.detail, name='detail'),
     url(r'^item_type/(?P<item_type_id>\d+)/$', views.item_type_detail, 
        name='item_type_detail'),
     url(r'^add_item$', views.add_item, name='add_item'),
     url(r'^add_item_type$', views.add_item_type, name='add_item_type'),
     url(r'^add_location$', views.add_location, name='add_location'),
)
