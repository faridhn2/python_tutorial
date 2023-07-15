from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

path = 'chromedriver.exe'

driver =webdriver.Chrome(executable_path=path)

driver.get('https://digikala.com')
time.sleep(10)

cart_a = WebDriverWait(driver, 100).until(EC.visibility_of_element_located((
    By.CSS_SELECTOR, '.pos-relative.d-inline-flex.py-2.pr-2.pl-0.p-2-lg.bg-000.radius')))
cart_a.send_keys(Keys.ESCAPE)


time.sleep(5)
driver.execute_script('window.scrollTo(0,500)')
time.sleep(2)
imgs = driver.find_elements(By.TAG_NAME,'img')

print(len(imgs))
for img in imgs:
    if img.get_attribute('alt')=='ورزش و سفر':
        src = img.get_attribute('src')
        print(src)
        img_data = requests.get(src).content
        with open('digi.png', 'wb') as handler:
            handler.write(img_data)
        break
