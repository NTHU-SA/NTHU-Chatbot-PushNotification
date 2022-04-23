# This is a daemon process. 
# https://pypi.org/project/python-daemon/ would be helpful.


# Periodically call the fetch messages. (time() /% 3600 == 0 -> run procedure)
### Fetch messages calls crawl.py

# Compare with sqlite database.

# Call backend API with messages which are not sent yet.