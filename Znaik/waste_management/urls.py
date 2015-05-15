from django.conf.urls import url

from . import views

urlpatterns = [
	#/waste_management
	url(r'^$', views.IndexView.as_view(), name = 'index'),
	# /waste_management/54
	url(r'^(?P<bin_id>[0-9]+)/$', views.detail, name = 'detail'),
	# /waste_management/54/waste_inside
	url(r'^(?P<bin_id>[0-9]+)/waste_inside/$', views.waste_inside, name = 'waste_inside'),
	# /waste_management/54/unload
	url(r'^(?P<bin_id>[0-9]+)/unload/$', views.unload, name = 'unload'),
]