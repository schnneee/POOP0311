#pip install selenium
#copy chromedriver (80ver) to c:\windows\system32
#chromedriver
#(ctrl+c!~!!!!!)
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys

browser = Chrome()
browser.get('https://www.python.org')

assert "Python" in browser.title
element = browser.find_element_by_name("q")
element.clear()
element.send_keys("tensorflow")
element.send_keys(Keys.RETURN)

# 取得ul下的所有li item
result = browser.find_elements_by_css_selector(".list-recent-events.menu")
allItems = result[0].find_elements_by_tag_name("li")
for r in allItems:
    content = r.find_elements_by_tag_name('a')
    print(content[0].text)
browser.close()