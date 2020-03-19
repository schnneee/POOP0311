# https://repo.anaconda.com/ install anaconda
import time

URL = 'https://www.momoshop.com.tw/main/Main.jsp'

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

browser = Chrome()
browser.get(URL)
element = browser.find_element_by_id("keyword")
element.clear()
element.send_keys("口罩")
element.send_keys(Keys.RETURN)

## get elements
#time.sleep(5) # 等網頁渲染
element = WebDriverWait(browser, 10).until( # 快的話不會等到10秒
    EC.presence_of_element_located((By.CLASS_NAME, "listArea"))
)
area = browser.find_element_by_class_name("listArea")
products = area.find_elements_by_class_name("goodsUrl")
print(len(products))
for product in products:
    print(product.get_property("href"))
    print(product.find_element_by_class_name("prdName").text)
browser.close()
