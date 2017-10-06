from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name = 'index'),

	#music/71 where 71 is id
	url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
]