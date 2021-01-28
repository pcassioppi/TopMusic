# TopMusic

This README is mostly so I can refer back to it for interview purposes, if you've made it here and your name doesn't rhyme with "Peter Cassioppi"....congrats.

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
#### Tools Used: BeautifulSoup, PyMongo, Spotify API

Once the users entered their username and POST-ed it to thje database through the frontend, the Change Stream would trigger a script to scrape the data for that user from Last.FM. The script scraped the users page and parsed their information using the BeautifulSoup library. The data for the users tracks, artists, and albums were all entered into the collections for their respective data in the MongoDB database using PyMongo.

Once the information for the user was entered into the database, the script would move on and retrieve the Spotify data for the tracks. These two were seperated so the user could see their Last.FM information on the frontend first, before the lengthy process of getting the Spotify data occurred (which was the slowest part of the program). First, the program checked if the track already had its info present in the database, if it didn't, the track was saved into an array to be entered into the Spotify scraper. The script would go to each tracks individual page and see if there was a Spotify link present, if there was, the Spotify ID was taken and used to retrieve the track data from Spotify's Developer API. This data was then stored on the database spotifyTrackData collection with the songs (slightly altered) last.fm link as it's id (this was chosen as the ID because it was also present in the users information, making it simple for the users track page to find it).

### LastFMDjango REST API
#### Tools Used: Django REST Framework, Djongo

The REST API was created to act as an interface between the MongoDB and the React frontend.
Views were created for tracks, albums, artists, users, and the spotify data.

The API framework I chose to use for this project was Django's REST Framework. I used Django both because I wanted experience with a major Python framework, and it had the support I needed to use the NoSQL MongoDB database I wanted to use. Though Django is made for a relational database, I was able to use the Djongo engine to make the framework mesh with MongoDB. Djongo translates the SQL queries made to the API as MongoDB queries, allowing the fromework and database to work together as if it were a relational database. 

### Frontend
#### Tools Used: React-Bootstrap, Axios, HTML

Components: Home/Form page, Artist Page, Track Page, Album Page, Track Spotify Data Page, Navigation bar

For the front end of the application I decided to use React because of its large usage in industry, and its ability to create dynamic web applications. Axios was the library used to make requests to the REST API. The front end allows users to POST their username, and GET their last.fm and Spotify track data. React-Bootstrap was used for many of the elements becauyse I think it looks nice :^) , and it is commonly used. This gave me good experience in what it is like to design a website so it is intuitive and looks good (and works lol).

Images (at the top right the username is saved after it is entered):

Home/Form Page:
![Alt](https://github.com/pcassioppi/TopMusic/blob/master/Screenshots/form.png)

Track Page:
![Alt](https://github.com/pcassioppi/TopMusic/blob/master/Screenshots/trackPage.png)

Track Spotify Data Page:
![Alt](https://github.com/pcassioppi/TopMusic/blob/master/Screenshots/SpotDataPage.png)

Artist Page:
![Alt](https://github.com/pcassioppi/TopMusic/blob/master/Screenshots/artistPage.png)

Album Page:
![Alt](https://github.com/pcassioppi/TopMusic/blob/master/Screenshots/albumPage.png)
