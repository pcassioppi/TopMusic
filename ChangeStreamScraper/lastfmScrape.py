#!/usr/bin/env python
# coding: utf-8

# TO DO:
# 1. Scrape the "https://www.last.fm/user/wiretable2/library/tracks" page. 
#     This page holds the persons top 45 tracks
#     SAVE IN DB:
#     track name
#     play count
#     artist
#     track link
#     more later....
# 2. Add the previous information into a database
# 3. Repeat process for: https://www.last.fm/user/wiretable2/library/albums and https://www.last.fm/user/wiretable2/library/artists
#     adding the new information to their own tables
# 4. Normalize data by creating and linking artist id's with tracks and albums instead of full names.
# 5. Extend the web scraper to run through the users TOTAL tracks/artists/albums by going through each page
#     ex. https://www.last.fm/user/wiretable2/library/artists?page=2
#     then add that new data to the database
# 6. Using each songs individual page on last.fm (ex. https://www.last.fm/music/Joy+Division/_/Disorder) find the spotify link for 
#     each song (these are under "Play this track" on the tracks page) and record its track data using spotify API



from requests import get
from bs4 import BeautifulSoup
import re


# 
# ![image.png](attachment:image.png)


#username = input("Enter username: ")





#Should try and scrape the page to get the value for z


def UserScrape(username):

    
    #creating loop to create urls for each page

    #initializing iterator variable
    z = 1

    #creating empty list for urls to be stored in
    t_urls = []

    #while the number of pages lower than 51
    #note: if a user does not have 50 pages of songs, last.fm just goes to their last page (92 for me)
    while z < 2:
        
        #generating url using format to insert the incrementing variable on each loop
        url = 'https://www.last.fm/user/{}/library/tracks?page={}'.format(username,z)

        
        #appending the url to the list of urls
        t_urls.append(url)
        
        #incrementing iterator variable so it can go to the next page
        z += 1




    #creating empty soup item to store the generated html files in
    html_soups_t = BeautifulSoup(features="lxml")

    for url in t_urls:
        
        #creating response to use in BeautifulSoup function
        response = get(url)
        
        #using the BeautifulSoup function on each response, appending the resulting soup object into the empty 'html_soups'
        html_soups_t.append(BeautifulSoup(response.text, 'html.parser'))


    tracks_og=[]
    tracks=[]
    names=[]
    link=[]
    artist=[]
    count=[]
    for _ in html_soups_t.find_all("td", class_="chartlist-name"):
        names.append(_.a['title'])
        link.append(_.a['href'])
    for _ in html_soups_t.find_all("td", class_="chartlist-artist"):
        artist.append(_.text.strip())
    for _ in html_soups_t.find_all("span", class_="chartlist-count-bar-value"):
        count.append(int(re.search(r'\d+',_.text.replace(',', '').strip()).group()))
    i=0

    while i < len(names):
        #tracks_og.append({'song_id':i, 'info':{'name':names[i], 'plays':count[i],'lfm_link':link[i], 'artist':artist[i]}})
        tracks.append({'song_id':i, 'name':names[i], 'plays':count[i],'lfm_link':link[i], 'artist':artist[i], 'user':username})
        i+=1





    #creating loop to create urls for each page

    #initializing iterator variable
    z = 1

    #creating empty list for urls to be stored in
    a_urls = []

    #note: if a user does not have the # of set pages, last.fm just goes to their last page 
    while z < 17:
        
        #generating url using format to insert the incrementing variable on each loop
        url = 'https://www.last.fm/user/wiretable2/library/artists?page={}'.format(z)

        
        #appending the url to the list of urls
        a_urls.append(url)
        
        #incrementing iterator variable so it can go to the next page
        z += 1



    #creating empty soup item to store the generated html files in
    html_soups_a = BeautifulSoup(features="lxml")

    for url in a_urls:
        
        #creating response to use in BeautifulSoup function
        response = get(url)
        
        #using the BeautifulSoup function on each response, appending the resulting soup object into the empty 'html_soups'
        html_soups_a.append(BeautifulSoup(response.text, 'html.parser'))




    artists=[]
    artists_og=[]
    name=[]
    count=[]
    link=[]
    for _ in html_soups_a.find_all("td", class_="chartlist-name"):
        name.append(_.a['title'])
        link.append(_.a['href'])
    for _ in html_soups_a.find_all("span", class_="chartlist-count-bar-value"):
        count.append(int(re.search(r'\d+',_.text.replace(',', '').strip()).group()))
    i=0
    while i < len(name):
        artists.append({'artist_id':i, 'name':name[i], 'plays':count[i],'lfm_link':link[i], 'user':username})
        i+=1




    #TIME TO DO THE ALBUMS SECTION
    #creating loop to create urls for each page

    #initializing iterator variable
    z = 1

    #creating empty list for urls to be stored in
    alb_urls = []

    #note: if a user does not have the # of set pages, last.fm just goes to their last page 
    while z < 2:
        
        #generating url using format to insert the incrementing variable on each loop
        url = 'https://www.last.fm/user/wiretable2/library/albums?page={}'.format(z)

        
        #appending the url to the list of urls
        alb_urls.append(url)
        
        #incrementing iterator variable so it can go to the next page
        z += 1



    #creating empty soup item to store the generated html files in
    html_soups_al = BeautifulSoup(features="lxml")

    for url in alb_urls:
        
        #creating response to use in BeautifulSoup function
        response = get(url)
        
        #using the BeautifulSoup function on each response, appending the resulting soup object into the empty 'html_soups'
        html_soups_al.append(BeautifulSoup(response.text, 'html.parser'))



    albums=[]
    album=[]
    artist=[]
    count=[]
    link=[]
    for _ in html_soups_al.find_all("td", class_="chartlist-name"):
        album.append(_.a['title'])
        link.append(_.a['href'])
    for _ in html_soups_al.find_all("td", class_="chartlist-artist"):
        artist.append(_.text.strip())
    for _ in html_soups_al.find_all("span", class_="chartlist-count-bar-value"):
        count.append(int(re.search(r'\d+',_.text.replace(',', '').strip()).group()))
    i=0
    while i < len(album):
        albums.append({'album_id':i, 'name':album[i], 'artist':artist[i],'plays':count[i],'lfm_link':link[i], 'user':username})
        i+=1




    if username == 'wiretable2':
        albums[34]['artist']='Travi$ Scott'




    import pandas as pd



    art_df=pd.json_normalize(artists).drop(columns=['plays','lfm_link','user'])
    alb_df=pd.json_normalize(albums).drop(columns=['album_id','name','plays','lfm_link','user'])
    tra_df=pd.json_normalize(tracks).drop(columns=['song_id','name','plays','lfm_link','user'])

    art_df=art_df.rename(columns={'name':'name'})

    alb_df=pd.merge(alb_df, art_df['artist_id'], how='left', left_on='artist', right_on=art_df['name'])
    #alb_df=alb_df.drop(columns=['artist'])

    tra_df=pd.merge(tra_df, art_df['artist_id'], how='left', left_on='artist', right_on=art_df['name'])
    #tra_df=tra_df.drop(columns=['artist'])



    alb_ids = alb_df['artist_id'].astype('float64')
    track_ids = tra_df['artist_id'].astype('float64')

    j=0
    for i in tracks:
        i['artist_id']=track_ids[j]
        #tracks[j] = {username:i}  
        # try:
        #     del i['artist']
        # except KeyError:
        #     pass
        j+=1


    j=0
    for i in albums:
        i['artist_id']=alb_ids[j]
        #albums[j] = {username:i}  
        # try:
        #     del i['artist']
        # except KeyError:
        #     pass
        j+=1



    import json
    from pymongo import MongoClient


    client = MongoClient()

    client = MongoClient('localhost', 27017)

    db = client.lastfm_db

    collection_alb = db.lastfm_album
    collection_art = db.lastfm_artist
    collection_t = db.lastfm_track


    for x in albums:
        if '_id' in x: 
            del x['_id'] 
        collection_alb.insert_one(x)



    for x in tracks:
        if '_id' in x: 
            del x['_id'] 
        collection_t.insert_one(x)

    for x in artists:
        if '_id' in x: 
            del x['_id']
        
        collection_art.insert_one(x)
