# TopMusic

I made this project to get better with Python and Javascript, as well as gain experience with new (to me) technologies, including Django, MongoDB, and React. I wanted to answer the question I've always had "How are complex websites really structured?", and I gained a lot of understanding of what goes into constructing a dynamic website. This included creating the NoSQL MongoDB database to store the information, the Django REST API to host the info, and the React frontend to display the information.


## Description
I started out wanting to find a way to connect my last.fm data with the spotify data for each track, and I thought it would be a good project to create a web app out of what I was doing. The spotify data that is displayed is a collection of "audio features" that spotify uses to analyze music and find similarities to make playlists or recommendations. For example, Danceability is how "danceable" a track is, valence is how "angry" the song is, etc..

The project takes a user entered last.fm username, and scrapes their last.fm library information to present their top 50 artists/albums/tracks, as well as retrieve the spotify audio data for the tracks in their library. (The top 50 number is arbitrary and the program could easily be expanded to cover their whole library, but this would of course increase latency significantly)

## Structure/Details
### MongoDB Database
#### Tools Used: Replica Set, Change Streams

The data for this project was stored in a MongoDB NoSQL database. I wanted to use a NoSQL/document database to store the information, because a) I wanted experience with it and b) I was unsure of the structure of the data, and I wanted the adaptability of a document database to adjust to any changes in the schemas. The schemaless design did get put into use when storiing the Spotify data, as some of the tracks didn't have the data available. The schema-less database allowed the inforrmation to not be stored with no wasted space used to store NULL values for the unretrievable data. 

In order to have the scraping functionality I wanted to use, I ended up using MongoDB's Change Streams as a trigger to scrape the users data and the Spotify info. Change Streams is a function that is provided by MongoDB that allows admins to see what changes are happening in their database, in real time. You can see details of each change made, including what data was just entered (like a username). I used this function to watch the "User" collection in the database and run the scraping script once a user POST-ed their username to the collection through the front end. This was done because I wanted to be able to scrape individual users in order to save space on the database.

A Replica Set is required in order to run the Change Streams function in MongoDB, since you want to be able to read and write to the database at the same time. In my case, the Change Stream is reading the database to see if any changes are occurring, and the API is also using the database to read/write any information it needs. 

### Change Streams Scraper



### Django REST API

### Frontend
