from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
path = 'chromedriver.exe'

driver =webdriver.Chrome(executable_path=path)

driver.get('https://fa.wikipedia.org/wiki/%D9%85%D9%87%D8%B1%D8%A7%D9%86_%D9%85%D8%AF%DB%8C%D8%B1%DB%8C')

h1 = driver.find_element(By.TAG_NAME,'h1')
print(h1)
print(h1.get_attribute('id'))
print(h1.get_attribute('class'))
print(h1.get_attribute('innerHTML'))
# tag : h1
# id : #id1
# class .class1
data_table = driver.find_element(By.CSS_SELECTOR,'.infobox.biography.vcard')

tbody = data_table.find_element(By.TAG_NAME,'tbody')
trs = tbody.find_elements(By.TAG_NAME,'tr')
print(len(trs))
th = trs[0].find_element(By.TAG_NAME,'th')
span_name = th.find_element(By.TAG_NAME,'span')
name = span_name.get_attribute('innerHTML')
with open('data.txt','w',encoding='utf-8') as fw:
    fw.write(name)
td_image = trs[1].find_element(By.TAG_NAME,'td')
anch = td_image.find_element(By.TAG_NAME,'a')
img = anch.find_element(By.TAG_NAME,'img')
image_src = img.get_attribute('src')
print(image_src)


img_data = requests.get(image_src).content
with open('image_name.jpg', 'wb') as handler:
    handler.write(img_data)

imgs = driver.find_elements(By.TAG_NAME,'img')
for idx,img in enumerate(imgs):
    src = img.get_attribute('src')
    img_data = requests.get(src).content
    with open(f'images/image_name{idx}.jpg', 'wb') as handler:
        handler.write(img_data)
