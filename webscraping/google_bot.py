from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.keys import Keys

path = 'chromedriver.exe'
op = webdriver.ChromeOptions()
op.add_argument("--incognito")
# op.add_argument("--headless")
driver =webdriver.Chrome(executable_path=path,chrome_options=op)

driver.get('https://google.com')
time.sleep(10)

search_input = WebDriverWait(driver, 100).until(EC.visibility_of_element_located((
    By.NAME, 'q')))


search_input.click()
search_input.send_keys('گربه اسکاتیش')
search_input.send_keys(Keys.ENTER)

divs = driver.find_elements(By.CSS_SELECTOR,'.Z26q7c.UK95Uc.jGGQ5e.VGXe8')
main_text = ''
for div in divs:
    a = div.find_element(By.TAG_NAME,'a')
    href = a.get_attribute('href')
    h3 = div.find_element(By.TAG_NAME,'h3')
    span = h3.find_element(By.TAG_NAME,'span')
    text = span.get_attribute('innerHTML')
    main_text += str(text)+'\n'
    main_text += str(href)+'\n'
with open('data2.txt','w',encoding='utf-8') as f:
    f.write(main_text)
    
     

