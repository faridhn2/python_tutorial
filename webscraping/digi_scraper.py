from selenium import webdriver
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
path='chromedriver.exe'
services = Service(executable_path = path)

class DigiScraper:
    def __init__(self,search_key):
        self.search_key = search_key
        self.driver = webdriver.Chrome(service=services)
        self.images = []
        self.prices = []
        self.links = []

    def process(self):
        self.driver.get(f'https://www.digikala.com/search/?q={self.search_key}')
        image_elements = WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'.w-full.rounded-medium.inline-block')))
        price_divs = WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'.flex.items-center.justify-end.gap-1.text-neutral-700.text-neutral-400.text-h5.grow')))
        product_divs = WebDriverWait(self.driver,10).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR,'.product-list_ProductList__item__LiiNI')))

        for prd_div ,img_elm , price_div in zip(product_divs,image_elements,price_divs):
            src = img_elm.get_attribute('src')
            self.images.append(src)

            price_span = price_div.find_element(By.TAG_NAME,'span')
            price = price_span.get_attribute('innerHTML')
            self.prices.append(price)

            anchor = prd_div.find_element(By.TAG_NAME,'a')
            href = anchor.get_attribute('href')
            self.links.append(href)

if __name__ == '__main__':
    dg_scr = DigiScraper('گوشی شیائومی')
    dg_scr.process()  
    print(dg_scr.prices)  
