from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import time

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
driver.get('http://staging/clickCount/')
count = driver.find_element_by_id("count")
button = driver.find_element_by_id("clickButton")

before = count.text
button.click()
after = count.text

print('Found: '+before + ' Then: ' + after)
driver.close()

assert int(before)+1 == int(after)
