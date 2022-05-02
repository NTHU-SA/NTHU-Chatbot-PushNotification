from ActiveNotification import insert
from ActiveNotification import exists
from ActiveNotification import openConnection
from ActiveNotification import closeConnection
from ActiveNotification import fetch

openConnection()
try:
    print("----- Initializer invoked -----")
    content = fetch(schools=['NTHU'])
    for item in content:
        if not exists(item):
            insert(item)
except Exception as e:
    print("Fatal error: " + str(e))
finally:
    closeConnection()
