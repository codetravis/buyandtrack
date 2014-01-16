from django.conf.urls import patterns, url

from items import views

urlpatterns = patterns('',
     url(r'^$', views.index, name='index'),
     url(r'^(?P<item_id>\d+)/$', views.detail, name='detail'),
     url(r'^category/(?P<item_type_id>\d+)/$', views.category_detail, 
        name='category_detail'),
     url(r'^add_item$', views.add_item, name='add_item'),
     url(r'^add_category$', views.add_category, name='add_category'),
     url(r'^add_location$', views.add_location, name='add_location'),
     url(r'^add_receipt$', views.add_receipt, name='add_receipt'),
     url(r'^monthly_report/(?P<year>\d+)/(?P<month>\d+)/$', views.monthly_report,
        name='monthly_report')
)
