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

search_btn = driver.find_element(By.XPATH,'//*[@id="base_layout_desktop_fixed_header"]/header/div[2]/div/div/div[1]/div/div/div[1]/div/span/div')
search_btn.click()
search_input = driver.find_element(By.XPATH,'//*[@id="base_layout_desktop_fixed_header"]/header/div[2]/div/div/div[1]/div/div/div[2]/div/div/div[1]/div/div/div/div/span/label/div/div/input')
search_input.send_keys('کتاب اثر مرکب')
time.sleep(2)
search_input.send_keys(Keys.ENTER)


