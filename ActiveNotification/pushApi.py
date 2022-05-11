import os
import time
import requests

url = "http://" + os.environ['SERVER_IP'] + ":" + os.environ['SERVER_PORT'] + "/"

def push_notification(msg):
    print(f"Pushing: {msg}")
    # return None
    
    audience = requests.get(url + "api/v1/user/getBroadcastAudienceIds").json()
    print(f"Audiences: {audience['msg']}")
    audience = audience['result']

    pushResult = requests.post(url + "api/v1/msg/push", data = {
        'to': audience, 
        'messages': [msg]
    }).json()
    print(f"Result: {pushResult['msg']}")
    pushResult = pushResult['result']

    ts = int(time.time()) 
    for uid in audience:
        upd = requests.post(url + "api/v1/user/updateBroadcastTag", data = {
            'userID': uid, 
            'tag': ts
        }).json()
        print(f"Update result: {upd['msg']}")



    