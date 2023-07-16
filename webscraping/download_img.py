from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys
browser = webdriver.Chrome()

browser.get('https://www.digikala.com/search/?q=%D8%B4%D8%A7%D8%B1%DA%98%D8%B1')

imgs = WebDriverWait(browser, 100).until(EC.visibility_of_all_elements_located((
    By.CSS_SELECTOR, '.w-100.radius-medium.d-inline-block.lazyloaded')))
for idx,img in enumerate(imgs):
    image_address = img.get_attribute('src')
    response = requests.get(image_address)
    print(response.content)
    with open('digi{}.png'.format(idx), 'wb') as file:
            file.write(response.content)



