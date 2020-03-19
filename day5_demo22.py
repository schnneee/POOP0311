URL = 'https://shopping.pchome.com.tw/'

from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

browser = Chrome()
browser.get(URL)
element = browser.find_element_by_id("keyword")
element.clear()
element.send_keys("¤f¸n")
element.send_keys(Keys.RETURN)

# element = browser.find_element_by_id("ItemContainer")
element = WebDriverWait(browser, 20).until(
    EC.presence_of_element_located((By.ID, "ItemContainer"))
)
print(type(element))
items = element.find_elements_by_class_name("col3f")
for item in items:
    nick = item.find_element_by_class_name("nick")
    print(nick.text)

browser.close()