# Import the required modules
from selenium import webdriver
from browsermobproxy import Server
import time
import json

har_file_path = "C:/Users/Soumya Mohanty/Downloads/www.facebook.com.har"
with open(har_file_path, "r", encoding="utf-8") as f:
    logs = json.loads(f.read())

# Store the network logs from 'entries' key and
# iterate them
network_logs = logs['log']['entries']
for log in network_logs:
    print(str(network_logs))
    # Except block will be accessed if any of the
    # following keys are missing
    try:
        # URL is present inside the following keys
        url = log['request']['url']

        # Checks if the extension is .png or .jpg
        if url[len(url) - 4:] == '.png' or url[len(url) - 4:] == '.jpg':
            print(url, end="\n\n")
    except Exception as e:
        # print(e)
        pass
