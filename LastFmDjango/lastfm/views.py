from django.shortcuts import render
import json
from django.core.serializers.json import DjangoJSONEncoder

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from lastfm.models import Artist, Album, Track, TrackSpotData, User
from lastfm.serializers import ArtistSerializer, AlbumSerializer, TrackSerializer, TrackSpotDataSerializer, UserSerializer
from rest_framework.decorators import api_view


# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def artist_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        artists = Artist.objects.all()
        
        artist_id = request.GET.get('artist_id', None)
        if artist_id is not None:
            artists = artists.filter(title__icontains=artist_id)
        
        artists_serializer = ArtistSerializer(artists, many=True)
        return JsonResponse(artists_serializer.data, safe=False)

    # elif request.method == 'POST':
    #     artist_data = JSONParser().parse(request)
    #     artist_serializer = ArtistSerializer(data=artist_data)
    #     if artist_serializer.is_valid():
    #         artist_serializer.save()
    #         return JsonResponse(artist_serializer.data, status=status.HTTP_201_CREATED) 
    #     return JsonResponse(artist_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
@api_view(['GET', 'PUT', 'DELETE'])
def artist_detail(request, pk):
    # find artist by pk (id)

    try: 
        artist = Artist.objects.get(pk=pk) 
    except Artist.DoesNotExist: 
        return JsonResponse({'message': 'The artist does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    
    if request.method == 'GET': 
        artist_serializer = ArtistSerializer(artist) 
        return JsonResponse(artist_serializer.data) 
    
    elif request.method == 'PUT': 
        artist_data = JSONParser().parse(request) 
        artist_serializer = ArtistSerializer(artist, data=artist_data) 
        if artist_serializer.is_valid(): 
            artist_serializer.save() 
            return JsonResponse(artist_serializer.data) 
        return JsonResponse(artist_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE':
        artist.delete() 
        return JsonResponse({'message': 'artist was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

    

######ALBUMS#######

@api_view(['GET', 'POST', 'DELETE'])
def album_list(request):
# def album_list(request,user):

    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        albums = Album.objects.all()
        # albums = Album.objects.get(user=user)
        
        album_id = request.GET.get('album_id', None)
        if album_id is not None:
            albums = albums.filter(title__icontains=album_id)
        
        albums_serializer = AlbumSerializer(albums, many=True)
        return JsonResponse(albums_serializer.data, safe=False)

    elif request.method == 'POST':
        album_data = JSONParser().parse(request)
        album_serializer = AlbumSerializer(data=album_data)
        if album_serializer.is_valid():
            album_serializer.save()
            return JsonResponse(album_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(album_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def album_detail(request, pk):
    # find tutorial by pk (id)

    try: 
        album = Album.objects.get(pk=pk) 
    except Album.DoesNotExist: 
        return JsonResponse({'message': 'The album does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    
    if request.method == 'GET': 
        album_serializer = AlbumSerializer(album) 
        return JsonResponse(album_serializer.data) 
    
    elif request.method == 'PUT': 
        album_data = JSONParser().parse(request) 
        album_serializer = AlbumSerializer(album, data=album_data) 
        if album_serializer.is_valid(): 
            album_serializer.save() 
            return JsonResponse(album_serializer.data) 
        return JsonResponse(album_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE':
        album.delete() 
        return JsonResponse({'message': 'album was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

#####TRACKS#########

@api_view(['GET', 'POST', 'DELETE'])
def track_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        tracks = Track.objects.all()
        
        # track_id = request.GET.get('track_id', None)
        # if track_id is not None:
        #     tracks = tracks.filter(title__icontains=track_id)
        
        tracks_serializer = TrackSerializer(tracks, many=True)
        return JsonResponse(tracks_serializer.data, safe=False)

    # elif request.method == 'POST':
    #     track_data = JSONParser().parse(request)
    #     track_serializer = TrackSerializer(data=track_data)
    #     if track_serializer.is_valid():
    #         track_serializer.save()
    #         return JsonResponse(track_serializer.data, status=status.HTTP_201_CREATED) 
    #     return JsonResponse(track_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# @api_view(['GET', 'PUT', 'DELETE'])
# def artist_detail(request, pk):
#     # find artist by pk (id)

#     try: 
#         artist = Artist.objects.get(pk=pk) 
#     except Artist.DoesNotExist: 
#         return JsonResponse({'message': 'The artist does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    
#     if request.method == 'GET': 
#         artist_serializer = ArtistSerializer(artist) 
#         return JsonResponse(artist_serializer.data) 
    
#     elif request.method == 'PUT': 
#         artist_data = JSONParser().parse(request) 
#         artist_serializer = ArtistSerializer(artist, data=artist_data) 
#         if artist_serializer.is_valid(): 
#             artist_serializer.save() 
#             return JsonResponse(artist_serializer.data) 
#         return JsonResponse(artist_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
#     elif request.method == 'DELETE':
#         artist.delete() 
#         return JsonResponse({'message': 'artist was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def track_detail(request, pk):
    # find tutorial by pk (id)

    try: 
        track = Track.objects.get(pk=pk) 
    except Track.DoesNotExist: 
        return JsonResponse({'message': 'The track does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    
    if request.method == 'GET': 
        track_serializer = TrackSerializer(track) 
        return JsonResponse(track_serializer.data) 
    
    elif request.method == 'PUT': 
        track_data = JSONParser().parse(request) 
        track_serializer = TrackSerializer(track, data=track_data) 
        if track_serializer.is_valid(): 
            track_serializer.save() 
            return JsonResponse(track_serializer.data) 
        return JsonResponse(track_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    
    elif request.method == 'DELETE':
        track.delete() 
        return JsonResponse({'message': 'track was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST', 'DELETE'])
def spotdata_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        spotdata = TrackSpotData.objects.all()        
        spotdata_serializer = TrackSpotDataSerializer(spotdata, many=True)
        return JsonResponse(spotdata_serializer.data, safe=False)

@api_view(['GET'])
def track_spot_data(request, primary_key):
    # find track data by pk (lfm_id)
    
    try: 
        spotData = TrackSpotData.objects.get(pk=primary_key) 
    except TrackSpotData.DoesNotExist: 
        return JsonResponse({'message': 'The data does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    
    if request.method == 'GET': 
        spotData_serializer = TrackSpotDataSerializer(spotData) 
        return JsonResponse(spotData_serializer.data) 

@api_view(['GET'])
def user_track_data(request, user):
    
    #obtaining list ffrom queryset of the users tracks
    if request.method == 'GET':
        tracks = list(Track.objects.filter(user=user))        
        tracks_serializer = TrackSerializer(tracks, many=True)
        return JsonResponse(tracks_serializer.data, safe=False)

@api_view(['GET'])
def user_album_data(request, user):
    
    if request.method == 'GET':
        #obtaining list ffrom queryset of the users albums
        albums = list(Album.objects.filter(user=user))        
        albums_serializer = AlbumSerializer(albums, many=True)
        return JsonResponse(albums_serializer.data, safe=False)

@api_view(['GET'])
def user_artist_data(request, user):
    #obtaining list ffrom queryset of the users artists
    if request.method == 'GET':
        artists = list(Artist.objects.filter(user=user))        
        artists_serializer = ArtistSerializer(artists, many=True)
        return JsonResponse(artists_serializer.data, safe=False)

##########USER################
@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    if request.method == 'GET':
        users = User.objects.all()
        
        username = request.GET.get('username', None)
        if username is not None:
            users = users.filter(username__icontains=username)
        
        user_serializer = UserSerializer(users, many=True)
        return JsonResponse(user_serializer.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


