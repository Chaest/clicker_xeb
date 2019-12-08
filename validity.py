from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True

driver = webdriver.Firefox(options=options)
driver.get('http://zigip.hopto.org:8054/clickCount/')
count = driver.find_element_by_id("count")
button = driver.find_element_by_id("clickButton")

before = count.text
button.click()
after = count.text

print(before + ' ' + after)
driver.close()

assert int(before)+1 == int(after)
