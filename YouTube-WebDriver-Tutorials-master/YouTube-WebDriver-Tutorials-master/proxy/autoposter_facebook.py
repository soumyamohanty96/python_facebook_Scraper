from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import geckodriver_autoinstaller

email = input('Enter your email: ')
password = input('Enter your password: ')
post = input('Enter your post: ')
geckodriver_autoinstaller.install()
driver = webdriver.Firefox()
wait = WebDriverWait(driver, 10)
driver.get('https://m.facebook.com/')
email_input = driver.find_element_by_xpath('//*[@id="m_login_email"]')
email_input.send_keys(email)
password_input = driver.find_element_by_xpath('//*[@id="m_login_password"]')
password_input.send_keys(password)
login_btn = driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[1]/div/div/div[2]/div/div[3]/form/div[5]/div[1]/button')
login_btn.click()
wait.until(EC.url_changes('https://m.facebook.com/'))
driver.get('https://m.facebook.com/')
whats_on_your_mind = driver.find_element_by_xpath('/html/body/div[1]/div/div[4]/div/div[1]/div[3]/div/div/div[1]/div/div[2]/div')
post_input = whats_on_your_mind.find_element_by_xpath('..')
post_input.click()
wait.until(EC.presence_of_element_located((By.ID, 'uniqid_1')))
post_text_area = driver.find_element_by_xpath('//*[@id="uniqid_1"]')
post_text_area.send_keys(post)
post_btn = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]/div/div/div[5]/div[3]/div/div/button')
post_btn.click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//*[contains(text(), 'Your post is now published.')]")))
print('Post published successfully!')
driver.quit()