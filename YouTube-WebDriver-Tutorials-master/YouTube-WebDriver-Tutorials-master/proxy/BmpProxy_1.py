import pprint
import time
from selenium import webdriver
import logging
import json
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
import os
import wget
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from datetime import datetime
from browsermobproxy import Server
from selenium import webdriver
import json
now = datetime.now()
dt_string = now.strftime("%d_%m_%y_%H%M%S")
file_name = "network_log"+dt_string+".json"

print(file_name)
keyword = input("Enter search group keyword:")


class ProxyManger:

    __BMP = "C:/browsermob-proxy-2.1.4-bin/browsermob-proxy-2.1.4/bin/browsermob-proxy.bat"

    def __init__(self):
        self.__server = Server(ProxyManger.__BMP)
        self.__client = None

    def start_server(self):
        self.__server.start()
        return self.__server

    def start_client(self):
        self.__client = self.__server.create_proxy(params={"trustAllServers": "true"})
        return self.__client

    @property
    def client(self):
        return self.__client

    @property
    def server(self):
        return self.__server


if "__main__" == __name__:


    options = webdriver.ChromeOptions()
    proxy = ProxyManger()

    client = proxy.start_client()
    client.new_har("facebook.com")
    server = proxy.start_server()

    #new driver related argument adding option properties
    #options = webdriver.ChromeOptions()
    #options.add_argument('--headless')


    options = webdriver.ChromeOptions()
    options.add_argument("--proxy-server={}".format(client.proxy))
    driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe',chrome_options=options)
    driver.get("https://www.facebook.com/")

    time.sleep(2)

   # target username
    username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='email']")))
    password = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='pass']")))

   # enter username and password
    username.clear()
    username.send_keys("9313807476")
    password.clear()
    password.send_keys("global@12345")
    button = WebDriverWait(driver, 2).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
    # We are logged in!
    time.sleep(1)
    # driver.get("https://www.facebook.com/search/top?q=groups")
    url = "https://www.facebook.com/search/groups?q=" + keyword
    driver.get(url)
    for j in range(0, 10):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        print(client.proxy)
        print("file_number1")
        #pprint.pprint(client.har)
        har_file = open(file_name,"w")
        har_file.write(str(client.har))

        #pprint.pprint(client.har)
    time.sleep(5)
    print("client_har_2")
    har_file.close()
    print("client_proxy")
    print("har_file_filteration//:")
    #pprint.pprint(client.har)

    har_file_path = "C:/Users/Soumya Mohanty/Downloads/www.facebook.com.har"
    with open(har_file_path, "r", encoding="utf-8") as f:
        logs = json.loads(f.read())

    # Store the network logs from 'entries' key and
    # iterate them
    network_logs = logs['log']['entries']
    for log in network_logs:
        file_data = open("Network_data.json","w")
        file_data.write(str(network_logs))

        print(str(network_logs))
        js_filter_data = open("data_latest.json", "w")
        js_filter_data.write(str(network_logs))
        js_filter_data.close()
        # Except block will be accessed if any of the
        # following keys are missing
        try:
            # URL is present inside the following keys
            url = log['request']['url']

            # Checks if the extension is .png or .jpg
            if url[len(url) - 4:] == '.png' or url[len(url) - 4:] == '.jpg':
                print(url, end="\n\n")
                file_data.write(str(url))
                js_filter_datas = open("data_latest1.json", "w")
                js_filter_datas.write(str(url))
                js_filter_datas.close()
        except Exception as e:
            # print(e)
            pass
        file_data.close()
    server.stop()