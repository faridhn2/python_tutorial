from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# path='chromedriver.exe'
# services = service(executable_path = path)
# browser =webdriver.Chrome(service = services)

# browser =webdriver.Chrome(executable_path = path)
chrome_option = webdriver.ChromeOptions()
# chrome_option.add_argument('--headless')

chrome_option.add_argument(r"--user-data-dir=C:\Users\Username\AppData\Local\Google\Chrome\User Data") 
# chrome_option.add_argument(r'--profile-directory=YourProfileDir') #e.g. Profile 3

# chrome_option.add_argument('--start-maximized')
# chrome_option.add_argument('--kiosk')
# chrome_option.add_argument('--start-fullscreen')
# chrome_option.add_argument('--incognito')
browser =webdriver.Chrome(options=chrome_option)
browser.get('https://www.digikala.com/')        

search_div = WebDriverWait(browser, 100).until(EC.visibility_of_element_located((
   By.CSS_SELECTOR, '.color-500.d-flex.ai-center.text-body-2')))




# search_div = browser.find_element(By.CSS_SELECTOR,'.color-500.d-flex.ai-center.text-body-2')

search_div.click()
time.sleep(2)
# search_input =WebDriverWait(browser, 100).until(By.XPATH , '//*[@id="modal-root"]/div[4]/div/div/div/div/div[1]/div/div/div/div/span/label/div/div/input')
search_input =WebDriverWait(browser, 100).until(EC.visibility_of_element_located((By.NAME , 'search-input')))

# search_input = browser.find_element(By.XPATH , r'//*[@id="base_layout_desktop_fixed_header"]/header/div[2]/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/span/label/div/div/input')
search_input.click()
search_input.send_keys('samsung')
search_input.send_keys(Keys.ENTER)

time.sleep(10)
h3_list =WebDriverWait(browser, 100).until(EC.visibility_of_all_elements_located((By.TAG_NAME , 'h3')))
text = ''
for h3 in h3_list:
   text += str(h3.text)
   text += '\n'
   # text += str(h3.get_attribute('innerHTML'))
   
# browser.close()
with open('titles.txt',mode='w+',encoding='UTF-8') as f:
   f.write(text)
# driver = webdriver.Chrome(executable_path=path)
# search_key = 'LG'
# driver.get('https://www.digikala.com/search/?q={}'.format(search_key))