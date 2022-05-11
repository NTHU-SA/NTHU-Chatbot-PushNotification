import os
import time
import requests

url = "http://" + os.environ['SERVER_IP'] + "/"

def push_notification(msg):
    print(f"Pushing: {msg}")
    # return None
    
    audience = requests.get(url + "api/v1/user/getBroadcastAudienceIds")
    print(f"Audiences: {audience}")

    pushResult = requests.post(url + "api/v1/msg/push", data = {
        'to': audience, 
        'messages': [msg]
    })
    print(f"Result: {pushResult}")

    ts = int(time.time()) 
    for uid in audience:
        upd = requests.post(url + "api/v1/user/updateBroadcastTag", data = {
            'userID': uid, 
            'tag': ts
        })
        print(f"Update result: {upd}")



    