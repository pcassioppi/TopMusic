from pymongo import MongoClient
from bson.json_util import dumps
import pymongo
import json

from lastfmScrape import UserScrape

# import sched, time
# s = sched.scheduler(time.time, time.sleep)
# # def do_something(sc): 
# #     print("Doing stuff...")
# #     # do your stuff
# #     s.enter(10, 1, do_something, (sc,))

# # s.enter(10, 1, do_something, (s,))
# # s.run()




client = MongoClient()

client = MongoClient('localhost', 27017)

db = client.lastfm_db

collection_alb = db.lastfm_album
collection_art = db.lastfm_artist
collection_t = db.lastfm_track
collection_user = db.lastfm_user

pipeline = [{'$match': {'operationType': 'insert'}}]
with collection_user.watch(pipeline) as stream:
    for insert_change in stream:
        username = insert_change['fullDocument']['username']
        # gets username from mongoDB and runs the lastfm scrape on it
        # collection_user.delete_one({'username':username})
        # collection_t.delete_many({'user':username})
        # collection_alb.delete_many({'user':username})
        # collection_art.delete_many({'user':username})
        UserScrape(username)
        #collection_user.delete_one({'username':username})


#print(collection_alb.count())
#test = {'username':username}

#collection_user.insert_one(test)

# z=db.artists_user




# i=0
# def do_something(sc):
   
#     q=z.count()
#     print(q)
#     # do your stuff
    

#     s.enter(10, 1, do_something, (sc,))

# s.enter(10, 1, do_something, (s,))
# s.run()

# with collection_alb.watch() as stream:
#     for change in stream:
#         print(change)

# for article in collection_alb.find().limit(5):
#      print(article)

# change_stream = client.changestream.collection_user.watch()
# for change in change_stream:
#     print(dumps(change))
#     print('') # for readability only

# try:
#     with collection_alb.watch([{'$match': {'operationType': 'insert'}}]) as stream:
#         for insert_change in stream:
#             # Do something
#             print(insert_change)
# except pymongo.errors.PyMongoError:
#     # The ChangeStream encountered an unrecoverable error or the
#     # resume attempt failed to recreate the cursor.
#     logging.error('...')

