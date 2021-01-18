from djongo import models

# Create your models here.
# after these are made: python manage.py makemigrations artists

# class ArtistInfo(models.Model):
#     name = models.CharField(max_length=70, blank=False, default='')
#     plays = models.PositiveIntegerField()
#     lfm_link = models.CharField(max_length=70, blank=False, default='')

class Artist(models.Model):
    artist_id = models.CharField(unique=True, max_length=100, primary_key=True)
    rank=models.PositiveIntegerField()
    name = models.CharField(max_length=70, blank=False, default='')
    plays = models.PositiveIntegerField(default=0)
    lfm_link = models.CharField(max_length=70, blank=False, default='')
    user = models.CharField(max_length=30, blank=False, default='')

class Album(models.Model):
    album_id = models.CharField(unique=True, max_length=100, primary_key=True)
    rank=models.PositiveIntegerField()
    name = models.CharField(max_length=70, blank=False, default='')
    plays = models.PositiveIntegerField(default=0)
    artist = models.CharField(max_length=70, blank=False, default='')
    lfm_link = models.CharField(max_length=70, blank=False, default='')
    # artist_id = models.PositiveIntegerField()
    user = models.CharField(max_length=30, blank=False, default='')

    #ordering by name. This may help with a search
    # class Meta:
    #     ordering = ['name']
    
    #artist_test = models.EmbeddedField
    #artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    #foreign key testing. to get this to work may need to add return values to Artist class
    #artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Track(models.Model):
    rank = models.PositiveIntegerField()
    track_id = models.CharField(unique=True, max_length=100, primary_key=True)
    name = models.CharField(max_length=70, blank=False, default='')
    plays = models.PositiveIntegerField(default=0)
    artist = models.CharField(max_length=70, blank=False, default='')
    lfm_link = models.CharField(max_length=70, blank=False, default='')
    user = models.CharField(max_length=30, blank=False, default='')

    #ordering by name. This may help with a search
    # class Meta:
    #     ordering = ['name']
class TrackSpotData(models.Model):
    lfm_id = models.CharField(unique=True, max_length=100, primary_key=True)    
    danceability = models.FloatField(blank=True, default=None)
    energy = models.FloatField(blank=True, default=None)
    key = models.FloatField(blank=True, default=None)
    loudness = models.FloatField(blank=True, default=None)
    mode = models.FloatField(blank=True, default=None)
    speechiness = models.FloatField(blank=True, default=None)
    acousticness = models.FloatField(blank=True, default=None)
    instrumentalness = models.FloatField(blank=True, default=None)
    liveness = models.FloatField(blank=True, default=None)
    valence = models.FloatField(blank=True, default=None)
    tempo = models.FloatField(blank=True, default=None)
    duration_ms = models.FloatField(blank=True, default=None)
    time_signature = models.FloatField(blank=True, default=None)
    spot_id = models.CharField(max_length = 25,blank=True)


 
class User(models.Model):
    username = models.CharField(max_length=30, blank=False, default='')