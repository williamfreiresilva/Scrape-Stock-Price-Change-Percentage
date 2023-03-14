from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time
import requests

#CBX:CBEX6 | CBXTR:CBTR6 | CBX10:CBE11 | C10TR:CB103 | CBXPR:CBPR4 | CBXPL:CBEP2 | ADRPR:ADPR4

def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_argument("disable-blink-features=AutomationControlled")
  prefs = {"credentials_enable_service": False,"profile.password_manager_enabled": False}
  options.add_experimental_option("prefs", prefs)
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  options.add_experimental_option("prefs",{'profile.default_content_settings.cookies': True})
  

  driver = webdriver.Chrome(options = options)
  driver.get("https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6")
  return driver


def sms():
  url = 'https://api.telegram.org/bot<your_bot_token>/sendMessage'
  data = {'chat_id': '<your_chat_id>', 'text': 'Stock price is down more than .10%'}
  requests.post(url,data=data)

def main():
  driver = get_driver()
  driver.find_element(by='id',value='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll').click()
  time.sleep(4)
  element = driver.find_element(By.XPATH,value='//*[@id="app_indeks"]/section[1]/div/div/div[2]/span[2]').text
  element = float(re.search(r'(-|\+)\d+.\d+', element).group())
  if element < -.1:
    sms()
  
print(main())