from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()

preferences = {"download.default_directory": "E:\Development\Webdriver-Tutorials", "safebrowsing.enabled": "false"}

options.add_experimental_option("prefs", preferences)

driver = webdriver.Chrome(options=options)

driver.get("https://www.whatsapp.com/download/")
driver.find_element(By.XPATH, "//a[text() = 'Download for Windows']").click()
