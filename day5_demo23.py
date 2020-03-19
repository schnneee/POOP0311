from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

opts = Options()
opts.headless = True
assert opts.headless
browser = Chrome(options = opts)
browser.get('https://www.python.org')
# browser.get('https://www.perl.org')
assert "Python" in browser.title
element = browser.find_element_by_name("q")
element.clear()
element.send_keys("tensorflow")
element.send_keys(Keys.RETURN)

result = browser.find_elements_by_css_selector(".list-recent-events.menu")
allItems = result[0].find_elements_by_tag_name("li")
for r in allItems:
    content = r.find_elements_by_tag_name('a')
    print(content[0].text)
browser.close()