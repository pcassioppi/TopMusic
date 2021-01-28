from pymongo import MongoClient
from bson.json_util import dumps
import pymongo
import requests
import json

from requests import get
from bs4 import BeautifulSoup
import re




# UserScrape(user)

# base_url = 'https://www.last.fm/user/{}/library/{}?page='
def scrapeUserData(username):

    def UserInfo(element,username):
    ##SHould work for all three
        def getNamesAndLinks(j,ret,soup):
            i=j
            for _ in soup.find_all("td", class_="chartlist-name"):
                ret.append({'name': _.a['title']})
                ret[i]['lfm_link']=_.a['href']
                i+=1

        def getPlays(element, j, ret, soup):
            i=j
            for _ in soup.find_all("span", class_="chartlist-count-bar-value"):
                ret[i][element+'_id']=username+':'+str(i)
                ret[i]['plays']=int(re.search(r'\d+',_.text.replace(',', '').strip()).group())
                ret[i]['user']=username
                ret[i]['rank'] = i
                i+=1

        def getTrackAlbArtists(j, ret, soup):
            i=j
            for _ in soup.find_all("td", class_="chartlist-artist"):
                ret[i]['artist']=_.text.strip()
                i+=1

        ##ADD THIS TO FRONT: https://lastfm.freetls.fastly.net/i/u/64s/ to get image
        def getTrackArt(j, ret, soup):
                i=j
                for _ in soup.find_all("td", class_="chartlist-image"):
                    ret[i]['image'] = _.img['src'][42:]
                    i+=1
        ## for artists: https://lastfm.freetls.fastly.net/i/u/avat
        def getArtistAlbumArt(j, ret, soup):
            i=j
            for _ in soup.find_all("td", class_="chartlist-image"):
                ret[i]['image'] = _.span.img['src'][42:]
                i+=1

        def lfmInfo(element, username):
            ret=[]

            el_url = 'https://www.last.fm/user/{}/library/{}s?page='.format(username, element)
            urls = []

            for z in range(1,2):
                url = el_url+str(z)
                urls.append(url)

            #had to add the j to the i values so the previous pages arent replaced by the new ones
            j=0
            for url in urls:
                response = get(url)

                soup = BeautifulSoup(response.text, 'html.parser')     

                getNamesAndLinks(j,ret,soup)


                if element == 'track' or element=='album':
                    getTrackAlbArtists(j,ret,soup)
                if element =='track':
                    getTrackArt(j,ret,soup)
                else:
                    getArtistAlbumArt(j,ret,soup)

                getPlays(element, j, ret, soup)

                j+=len(ret)

            return ret
        return lfmInfo(element, username)


    artists = UserInfo('artist',username)
    albums = UserInfo('album',username)
    tracks = UserInfo('track',username)

    client = MongoClient()

    client = MongoClient('localhost', 27017)

    db = client.lastfm_db



    def insertUserInfo(db,tracks,albums,artists):
        # client = MongoClient()

        # client = MongoClient('localhost', 27017)

        # db = client.lastfm_db

        collection_alb = db.lastfm_album
        collection_art = db.lastfm_artist
        collection_t = db.lastfm_track
        collection_u = db.lastfm_user
        # collection_spotData = db.lastfm_spotData

        if collection_alb.count_documents({'user':username}) > 0:
            query = {'user': username}
            collection_alb.delete_many(query)
            collection_art.delete_many(query)
            collection_t.delete_many(query)
        
        for x in albums:
            if '_id' in x: 
                del x['_id'] 
            collection_alb.insert_one(x)
        for x in artists:
            if '_id' in x: 
                del x['_id']
            collection_art.insert_one(x)
        i=1
        for x in tracks:
            if '_id' in x: 
                del x['_id']
            x['rank'] = i
            
            collection_t.insert_one(x)
            i+=1


    insertUserInfo(db,tracks,albums,artists)

    CLIENT_ID = 'bb3e039f3beb46b18a253e93e8aaea8d'
    CLIENT_SECRET = '481055b4f0474fcf8eecf67f210b1489'

    def getSpotifyData(noDataTracks):
        def findSpotId(link):
            url = 'https://www.last.fm'+link

            soup = BeautifulSoup(get(url).text, 'html.parser')

            spot_id=None
            if soup.find('a',class_='visible-xs play-this-track-playlink play-this-track-playlink--spotify'):
                spot_id = soup.find('a',class_='visible-xs play-this-track-playlink play-this-track-playlink--spotify')['href'].split('/')[-1]
            return spot_id
        
        def getIds():
            

            ids = ''
        
            for song in noDataTracks:
        #         spot_id=None
                spot_id = findSpotId(song)
                if spot_id is None:
                    if '-' in song:
                        url = song.split('-')[0][:-1]
                        spot_id = findSpotId(url)
                    elif '(' in song:
                        url = song.split('(')[0][:-1]
                        spot_id = findSpotId(url)
                    elif '%' in song:
                        url = song.split('%')[0][:-1]
                        spot_id = findSpotId(url)

                if spot_id is not None:
                    ids = ids + ','+ spot_id

                else:
                    ids = ids+','
            return ids[1:]
        
        def getSpotInfo(ids, CLIENT_ID, CLIENT_SECRET):
            AUTH_URL = 'https://accounts.spotify.com/api/token'

            auth_response = requests.post(AUTH_URL, {
                'grant_type': 'client_credentials',
                'client_id': CLIENT_ID,
                'client_secret': CLIENT_SECRET,
            })

            auth_response_data = auth_response.json()

            access_token = auth_response_data['access_token']

            headers = {
                'Authorization': 'Bearer {token}'.format(token=access_token)
            }

            BASE_URL = 'https://api.spotify.com/v1/'
            data = requests.get(BASE_URL + 'audio-features/?ids=' + ids, headers=headers)

            return data.json()
        
        def assignTrackData():
            ret = []
    #         if len(data['audio_features'])==0:
    #             return ret
            
            for i in range(len(data['audio_features'])):
                ret.append({'lfm_id':noDataTracks[i]})
                ret[i]['image']=tracks[i]['image']
                feat = data['audio_features'][i]
                if feat:
                    for j in feat:
                        ret[i][j]=feat[j]
                
            return ret

        ids = getIds()
        data = getSpotInfo(ids, CLIENT_ID, CLIENT_SECRET)
                
        out = assignTrackData()
        
        return out


    def InsertTracks(db):
    

        collection_t = db.lastfm_track
        
        
        collection_spotData = db.lastfm_trackspotdata
        userTrackIds = []
        for article in collection_t.find({'user':username}):
            userTrackIds.append(article['lfm_link'])
        noDataTracks =[]
        
        for s in userTrackIds:
            # checking if there are no documents with the lfm link in the database, if they aren't, append them to list
            if collection_spotData.count_documents({'lfm_id':s[7:].replace('/','').replace('%','')}) == 0:
                noDataTracks.append(s)
    #     return noDataTracks
        spotData =[]
        if len(noDataTracks)>0:
            spotData=getSpotifyData(noDataTracks)
        
        for x in spotData:
            if '_id' in x: 
                del x['_id']
            if 'id' in x:
                x['spot_id']=x['id']
            else:
                x['spot_id']=''
            #have to replace these characters so the links will work for API url
            x['lfm_id'] = x['lfm_id'][7:].replace('/', '').replace('%', '')
            
            collection_spotData.insert_one(x)
        
    # if len(noDataTracks)>0:
    #     spotData=getSpotifyData(noDataTracks)
    InsertTracks(db)

