from rest_framework import serializers 
from lastfm.models import Artist, Album, Track, TrackSpotData, User


# class ArtistInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ArtistInfo
#         fields =['name','plays','lfm_link']


class ArtistSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Artist
        fields = (#'_id',
                    'artist_id',
                    'rank',
                    'name',
                    'plays',
                    'lfm_link',
                    'image',
                    'user')

class AlbumSerializer(serializers.ModelSerializer):
 
    class Meta:
        
        model = Album
        fields = (#'_id',
                    'album_id',
                    'rank',
                    'name',
                    'plays',
                    'artist',
                    'lfm_link',
                    'image',
                    # 'artist_id',
                    'user')
        

class TrackSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Track
        fields = (#'_id',
                    'rank',
                    'track_id',
                    'name',
                    'plays',
                    'artist',
                    'lfm_link',
                    'image',
                    'user')

class TrackSpotDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackSpotData
        fields = (
                'lfm_id',
                'image',
                'danceability',
                'energy',
                'key',
                'loudness',
                'mode',
                'speechiness',
                'acousticness',
                'instrumentalness',
                'liveness',
                'valence',
                'tempo',
                'duration_ms',
                'time_signature',
                'spot_id'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (#'id', 
                    'username',)
