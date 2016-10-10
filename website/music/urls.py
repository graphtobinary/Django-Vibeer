from django.conf.urls import include, url
from . import views

app_name = 'music'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name = 'index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name = 'detail'),
    #view for album add
    url(r'^album/add/$', views.AlbumCreate.as_view(), name = 'album-add'),
    #view for album update
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name = 'album-update'),
    #view for album delete
    url(r'^album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name = 'album-delete'),
    #url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name = 'favorite'),
]
