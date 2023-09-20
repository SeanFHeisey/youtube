# Sean Heisey
# 9/20/2023
# Refresh Token (if token from youtubeUploadSEO expires run this code)

import os
from google_auth_oauthlib.flow import InstalledAppFlow
import json

# remove token file
if os.path.exists("C:/xxxxx/xxxxx/xxxxx/token files/token_youtube_v3.json"): # locate token, example: C:/xxxxx/xxxxx/xxxxx/token files/token_youtube_v3.json
    os.remove("C:/xxxxx/xxxxx/xxxxx/token files/token_youtube_v3.json") # remove token, example: C:/xxxxx/xxxxx/xxxxx/token files/token_youtube_v3.json

# change json name
old_name = r"C:/xxxxx/xxxxx/xxxxx/client_secret_9999999999-xxxxxxxxxx.apps.googleusercontent.com.json" # example C:/xxxxx/xxxxx/xxxxx/client_secret_9999999999-xxxxxxxxxx.apps.googleusercontent.com.json
new_name = r"C:/xxxxx/xxxxx/xxxxx/client_secret.json" # example C:/xxxxx/xxxxx/xxxxx/client_secret.json
os.rename(old_name, new_name) # renames old file to new file name

# create new json file
file = "client_secret.json" 

# changes new json file to old file name and dumps contents from old file
def write_json(data, filename="client_secret_9999999999-xxxxxxxxxx.apps.googleusercontent.com.json"): # example C:/xxxxx/xxxxx/xxxxx/client_secret_9999999999-xxxxxxxxxx.apps.googleusercontent.com.json
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)

with open(file, "r") as json_file:
    data = json.load(json_file)
    write_json(data)

# deletes old json file
if os.path.exists("C:/xxxxx/xxxxx/xxxxx/client_secret.json"): # if old json file exists, example: C:/xxxxx/xxxxx/xxxxx/client_secret.json
    os.remove("C:/xxxxx/xxxxx/xxxxx/client_secret.json") # remove old json file, example: C:/xxxxx/xxxxx/xxxxx/client_secret.json

# token refreshed
print('token refreshed') # 0 errors
exit()
