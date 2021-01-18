from rest_framework import serializers 
from lastfm.models import Artist, Album, Track, TrackSpotData, User


# class ArtistInfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ArtistInfo
#         fields =['name','plays','lfm_link']


# class ArtistSerializer(serializers.ModelSerializer):
#     info = ArtistInfoSerializer(many=True)

#     class Meta:
#         model=Artist
#         fields = ['artist_id','info']
    
#     def create(self, validated_data):
#         artist_info_data = validated_data.pop('info')
#         artist = Artist.objects.create(**validated_data)
#         for info_data in artist_info_data:
#             ArtistInfo.objects.create(artist=artist, **info_data)
#         return artist

class ArtistSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Artist
        fields = (#'_id',
                    'artist_id',
                    'rank',
                    'name',
                    'plays',
                    'lfm_link',
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
                    'user')

class TrackSpotDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TrackSpotData
        fields = (
                'lfm_id',
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
