from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import service
import time
path='chromedriver.exe'
# services = service(executable_path = path)
# browser =webdriver.Chrome(service = services)

browser =webdriver.Chrome(executable_path = path)
browser.get('https://www.google.com/')
# time.sleep(5)
# browser.close()
search_input = browser.find_element(By.NAME,'q')
id = search_input.get_attribute('id')
print(id)
# time.sleep(10)
search_input.click()
search_input.send_keys('رازهایی در مورد گربه ها')
search_input.send_keys(Keys.ENTER)
time.sleep(10)
blocks = browser.find_elements(By.CLASS_NAME,'tF2Cxc')
# text = ''
# for div in blocks:
#     text+=div.get_attribute('innerHTML')
#     text+='\n'
# with open('blocks.txt',mode='w+',encoding='UTF-8') as f:
#     f.write(text)
links = []
for div in blocks:
    a = div.find_element(By.TAG_NAME,'a')
    h = a.get_attribute('href')
    links.append(h)

print(links)
for link in links:
    browser.get(link)
    time.sleep(10)
