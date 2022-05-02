import time
import os
from ActiveNotification import insert
from ActiveNotification import exists
from ActiveNotification import openConnection
from ActiveNotification import closeConnection
from ActiveNotification import fetch
from ActiveNotification import push

# Periodically call the fetch messages. (time() % 3600 == 0 -> run procedure)

while True:
    openConnection()
    try:
        while int(time.time())  % int(os.environ['PERIOD']) != 0:
            time.sleep(1)
        print("----- Daemon invoked -----")
        content = fetch(schools=['NTHU'])
        for item in content:
            if not exists(item):
                push(item)
                insert(item)
    except Exception as e:
        print("Reboot. Fatal error: " + str(e))
    finally:
        closeConnection()
