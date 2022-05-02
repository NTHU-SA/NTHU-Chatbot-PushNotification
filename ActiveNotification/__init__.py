import ActiveNotification.fetchMessages
import ActiveNotification.getDifferences
import ActiveNotification.pushApi

differences = ActiveNotification.getDifferences.getDifferences()

fetch = ActiveNotification.fetchMessages.fetch_messages
exists = differences.exists
insert = differences.insert
openConnection = differences.open
closeConnection = differences.close
push = ActiveNotification.pushApi.push_notification