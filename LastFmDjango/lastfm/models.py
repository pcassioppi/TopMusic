from djongo import models

# Create your models here.
# after these are made: python manage.py makemigrations artists

# class ArtistInfo(models.Model):
#     name = models.CharField(max_length=70, blank=False, default='')
#     plays = models.PositiveIntegerField()
#     lfm_link = models.CharField(max_length=70, blank=False, default='')

class Artist(models.Model):
    artist_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=70, blank=False, default='')
    plays = models.PositiveIntegerField(default=0)
    lfm_link = models.CharField(max_length=70, blank=False, default='')
    user = models.CharField(max_length=30, blank=False, default='')

class Album(models.Model):
    album_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=70, blank=False, default='')
    plays = models.PositiveIntegerField(default=0)
    artist = models.CharField(max_length=70, blank=False, default='')
    lfm_link = models.CharField(max_length=70, blank=False, default='')
    artist_id = models.PositiveIntegerField()
    user = models.CharField(max_length=30, blank=False, default='')

    #ordering by name. This may help with a search
    # class Meta:
    #     ordering = ['name']
    
    #artist_test = models.EmbeddedField
    #artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    #foreign key testing. to get this to work may need to add return values to Artist class
    #artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

class Track(models.Model):
    song_id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=70, blank=False, default='')
    plays = models.PositiveIntegerField(default=0)
    artist = models.CharField(max_length=70, blank=False, default='')
    lfm_link = models.CharField(max_length=70, blank=False, default='')
    artist_id = models.PositiveIntegerField()
    user = models.CharField(max_length=30, blank=False, default='')

    #ordering by name. This may help with a search
    # class Meta:
    #     ordering = ['name']

class User(models.Model):
    username = models.CharField(max_length=30, blank=False, default='')