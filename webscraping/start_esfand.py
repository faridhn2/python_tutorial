from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
path='chromedriver.exe'
services = Service(executable_path = path)
op = webdriver.ChromeOptions()
# op.add_argument("--incognito")
# op.add_argument("--start-maximized")
# op.add_argument(r"--user-data-dir=C:\Users\Farid\AppData\Local\Google\Chrome\User Data") 
# op.add_argument('--start-maximized')
# op.add_argument('--kiosk')
# op.add_argument('--start-fullscreen')
# op.add_argument('--incognito')
# op.add_argument("--headless")
browser = webdriver.Chrome(service=services,options=op)

# browser.get('https://google.com')
# search_input = browser.find_element(By.NAME,'q')
# search_input.click()
# time.sleep(2)
# search_input.send_keys('cat')
# time.sleep(2)
# search_input.send_keys(Keys.ENTER)
# time.sleep(10)

browser.get('https://digikala.com')
time.sleep(400)
search_btn = browser.find_element(By.CSS_SELECTOR,'.text-neutral-500.flex.items-center.text-body-2')
search_btn.click()
time.sleep(2)
search_input = browser.find_element(By.NAME,'search-input')
search_input.click()
search_input.send_keys('موبایل سامسونگ')
search_input.send_keys(Keys.ENTER)
time.sleep(2)
# products = browser.find_elements(By.CLASS_NAME,'product-list_ProductList__item__LiiNI')
for i in range(1,10):
    browser.execute_script(f'window.scrollTo(0,{500*i})')
    time.sleep(2)
products = WebDriverWait(browser, 100).until(EC.visibility_of_all_elements_located((
        By.CLASS_NAME,'product-list_ProductList__item__LiiNI')))
prd_dict = {}

for idx, product in enumerate(products):
    try:
        print('----------------------')
        
        anchor = WebDriverWait(product, 5).until(EC.visibility_of_element_located((
        By.TAG_NAME, 'a')))
        h3 = WebDriverWait(product, 5).until(EC.visibility_of_element_located((
        By.TAG_NAME, 'h3')))
        
        link = anchor.get_attribute('href')
        title = h3.get_attribute('innerHTML')
        prd_dict[title] = link
        img_el = product.find_element(By.CSS_SELECTOR,'.w-full.rounded-medium.inline-block')
        src = img_el.get_attribute('src')
        response = requests.get(src)
        
        with open(f'images/my_img_{idx}.jpg','wb') as f:
            f.write(response.content)
        # print(product.get_attribute('innerHTML'))
        # print(title)
        print('----------------------')
        # print(prd_dict)
    except:
        pass
print(prd_dict)
with open('products.txt','w+',encoding='UTF-8') as f :
    f.write(str(prd_dict))
time.sleep(10)
