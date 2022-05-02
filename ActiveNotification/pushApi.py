import os
import requests

url = os.environ['SERVER_URL']

def push_notification(msg):
    print(f"Pushed: {msg}")
    return None
    myobj = {'somekey': 'somevalue'}
    audience = requests.post(url + "/getBroadcastAudienceIds", data = myobj)
    print(x.text)
    pushResult = requests.post(url + "/msg/push", data = myobj)
    print()
    x = requests.post(url + "/updateBroadcastTag", data = myobj)

    