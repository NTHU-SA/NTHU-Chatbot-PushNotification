# This is a daemon process. 
# https://pypi.org/project/python-daemon/ would be helpful.
from ActiveNotification.fetchMessages import fetch_messages
from ActiveNotification.getDifferences import *

# Periodically call the fetch messages. (time() /% 3600 == 0 -> run procedure)

content = fetch_messages(school='NTHU')
for item in content:
    if not exists(item):
        # Push
        insert(item)
