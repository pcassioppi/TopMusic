from django.conf.urls import url 
from lastfm import views 
 
urlpatterns = [ 
    url(r'^api/artists$', views.artist_list),
    url(r'^api/artists/(?P<pk>[0-9]+)$', views.artist_detail),
    url(r'^api/albums$', views.album_list),
    url(r'^api/albums/(?P<pk>[0-9]+)$', views.album_detail),
    url(r'^api/tracks$', views.track_list),
    url(r'^api/tracks/(?P<pk>[0-9]+)$', views.track_detail),
    url(r'^api/users$', views.user_list),
    #url(r'^api/albums/(?P<pk>[0-9]+)$', views.album_detail),
    #url(r'^api/tutorials/published$', views.tutorial_list_published)
]