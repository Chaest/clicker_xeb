from selenium import webdriver
from selenium.webdriver.firefox.options import Options

import time

# Wait a bit to make sure the app is deployed
time.sleep(4)

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
driver.get('http://zigip.hopto.org:8054/clickCount/')
# Handles latency due to poor host performances
time.sleep(6)
count = driver.find_element_by_id("count")
button = driver.find_element_by_id("clickButton")

before = count.text
button.click()
# Handles latency due to poor host performances
time.sleep(2)
after = count.text

print('Found: '+before + ' Then: ' + after)
driver.close()

assert int(before)+1 == int(after)
