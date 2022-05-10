import os
import time
import requests

url = "http://" + os.environ['SERVER_IP'] + "/"

def push_notification(msg):
    print(f"Pushing: {msg}")
    # return None
    
    audience = requests.get(url + "v1/user/getBroadcastAudienceIds")
    print(audience)

    pushResult = requests.post(url + "v1/msg/push", data = {
        'to': audience, 
        'messages': [msg]
    })
    print(pushResult)

    ts = int(time.time()) 
    for uid in audience:
        upd = requests.post(url + "v1/user/updateBroadcastTag", data = {
            'userID': uid, 
            'tag': ts
        })
        print(upd)


    