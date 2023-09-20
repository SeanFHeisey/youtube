# Sean Heisey
# 9/20/2023
# YouTube Upload and SEo Optimization for Type Beat Channels

import sys
import requests
from rapid_tags import RapidTags
import datetime
from googleapiclient.http import MediaFileUpload
from google_apis import create_service
from youtube import YouTube

# input with sys
print("Enter YouTube Video Title: ")
title = sys.stdin.readline() # example: [FREE] Drake x Rod Wave Type Beat - "Name"
print("Enter Key: ")
descKey = sys.stdin.readline()
print("Enter BPM: ")
BPM = sys.stdin.readline()

# pull Rapidtags from YouTube title
rapidTags = ""
i = 7 # iterates through '[FREE] '
while i < len(title):
    if(title[i]==' ' and title[i+1]=='T' and 
       title[i+2]=='y' and title[i+3]=='p' and title[i+4]=='e'):
        break # stop iterating at ' Type'
    if(title[i]==' ' and title[i+1]=='x' and title[i+2]==' ' or
       title[i]==' ' and title[i+1]=='X' and title[i+2]==' '):
        i += 1 # skip over ' x ' or ' X '
    else:
        rapidTags += title[i] # Rapidtags string
    i += 1

# pull tags from Rapidtags
finalRapidTags = RapidTags.get_tags_cls(rapidTags) # search tags using rapid_tags API using RapidTags string pulling YouTube tags
tags = str(finalRapidTags).replace("'", "").replace("[", "'").replace("]", "'").replace("'", "") # removes unwanted characters

# YouTube description (SEO optimized)
description = (title +
               "\nBEATS ARE FREE FOR NON-PROFIT USE ONLY" +
               "\nMUST CREDIT: \"Prod. MangoBeats\" In Song & Video Title" +
               "\n\nKey: " + descKey +
               "BPM: " + BPM +
               "\nYouTube - https://www.youtube.com/@prodMangoBeats" +
               "\nPlaylist - https://www.youtube.com/playlist?list=PLUSy0pkCn4iPX3HzbVSlYMuXvgr3IqndY" +
               "\nInstagram - https://www.instagram.com/prod.mangobeats/" +
               "\nEmail - meep4@frontier.com\n\n" +
               "ignore tags:\n" +
               tags)

# handling large mp4 files using requests
requests.get('http://google.com', timeout=(60, 300)) # 60 seconds to connect to server, 300 seconds until timeout
requests.get('http://youtube.com', timeout=(60, 600))# 60 seconds to connect to server, 600 seconds until timeout

# video upload categories
def video_categories():
    video_categories = service.videoCategories().list(part='snippet', regionCode='US').execute()
    df = pd.DataFrame(video_categories.get('items'))
    return pd.concat([df['id'], df['snippet'].apply(pd.Series)[['title']]], axis=1)

# YouTube Data API v3 using create_service
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube']
client_file = 'client_secret_xxxxxxxxxx.apps.googleusercontent.com.json'
service = create_service(client_file, API_NAME, API_VERSION, SCOPES)

# upload video using datetime
upload_time = (datetime.datetime.now() + datetime.timedelta(days=0)).isoformat() + '.000Z'
request_body = {
    'snippet': {
        'title': title,
        'description': description,
        'categoryId': '10',
        'tags': [tags]
    },
    'status': {
        'privacyStatus': 'private',
        'publishedAt': upload_time,
        'selfDeclaredMadeForKids': False
    },
    'notifySubscribers': True
}

# video you want to upload
video_file = 'C:/xxxxx/xxxxx/xxxxx/xxxxx/xxxxx/xxxxxxxxxx.mp4' # example: 'C:/xxxxx/xxxxx/xxxxx/xxxxxxxxxxxxxxxx.mp4'

# uploading video using MediaFileUpload
media_file = MediaFileUpload(video_file)
response_video_upload = service.videos().insert(
    part='snippet,status',
    body=request_body,
    media_body=media_file
).execute()
uploaded_video_id = response_video_upload.get('id')

# add uploaded video to playlist using YouTube
yt = YouTube(client_file)
yt.init_service()
target_playlist_id = 'xxxxxxxxxxxxxxxxxxxx' # example (enter the x's): https://www.youtube.com/watch?v=9999999999&list=xxxxxxxxxx
request_body = {
    'snippet': {
        'playlistId': target_playlist_id,
        'resourceId': {
            'kind': 'youtube#video',
            'videoId': uploaded_video_id
        }
    }
}
response = yt.service.playlistItems().insert(
    part='snippet',
    body=request_body
).execute()
video_title = response['snippet']['title']
print('Video inserted to playlist') # 0 errors
exit() # upload complete
