from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.action_chains import ActionChains

PATH = 'chromedriver.exe'

##### Handling of Allow Pop Up In Facebook
option = Options()
option.add_argument("--disable-infobars")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 2
})

driver = webdriver.Chrome(executable_path='C:/webdrivers/chromedriver.exe', chrome_options=option)
driver.maximize_window()
driver.get("https://www.facebook.com/")


###Login To The Account
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

#### Post Content On FaceBook

button = driver.find_element_by_class_name("sx_0b6f88").click()
time.sleep(3)  ## A 3 second break in the program so that everythin loads perfectly
actions = ActionChains(driver)  ##Action Chains
actions.send_keys(Keys.TAB)  ##Press TAB
actions.send_keys(Keys.ENTER)  ##Press ENTER
actions.send_keys("I am Sakshi.//:")
actions.send_keys(Keys.TAB * 10)  ### Press TAB 10 Times to reach POST button
actions.send_keys(Keys.ENTER)  ### Press ENTER to post the content on facebook
actions.perform()  ## To perfrom all the operations in the action chains

