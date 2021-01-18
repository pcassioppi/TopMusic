from django.urls import path
from lastfm import views 
 
urlpatterns = [ 
    # path('api/artists', views.artist_list),
    # path('api/artists/<int:pk>', views.artist_detail),
    # path('api/albums', views.album_list),
    # url(r'^api/albums/(?$', views.album_list),
    # path('api/albums/<int:pk>', views.album_detail),
    # url(r'^api/tracks$', views.track_list),
    # url(r'^api/tracks/(?P<pk>[0-9]+)$', views.track_detail),
    # path('api/tracks',views.track_list),
    # path('api/tracks/<int:pk>',views.track_detail),
    path('api/users', views.user_list),
    path('api/spotdata', views.spotdata_list),
    path('api/spotdata/<str:primary_key>', views.track_spot_data),
    path('api/userdata/tracks/<str:user>', views.user_track_data),
    path('api/userdata/artists/<str:user>', views.user_artist_data),
    path('api/userdata/albums/<str:user>', views.user_album_data)

]