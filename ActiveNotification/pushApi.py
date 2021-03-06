import os
import time
import requests

url = "http://" + os.environ['SERVER_IP'] + ":" + os.environ['SERVER_PORT'] + "/"

def push_notification(msg):
    print(f"Pushing: {msg}")
    # return None
    
    audience = requests.get(url + "api/v1/user/getBroadcastAudienceIds").json()
    print(f"Audience msg: {audience['msg']}")
    print(f"Audiences: {audience['result'][:5]}")
    audience = audience['result']

    msg = f"{msg['school']} - {msg['dep']} - {msg['category']}：\n{msg['title']}\n{msg['url']}"
    for i in range(0, len(audience), 500):
        payload = {
            'to': audience[i:i+500], 
            'messages': [{
                "type": "text",
                "text": msg
            }]
        }
        pushResult = requests.post(url + "api/v1/msg/push", json=payload).json()
        print(f"Result: {pushResult}")

    ts = int(time.time()) 
    for uid in audience:
        upd = requests.post(url + "api/v1/user/updateBroadcastTag", data = {
            'userID': uid, 
            'tag': ts
        }).json()
        print(f"Update result: {upd['msg']}")
    