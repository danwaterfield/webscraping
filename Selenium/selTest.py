import time
from selenium import webdriver

# currently broken, trying to figure out the path to the chromedriver executable. grrgrgrgrgrg

driver = webdriver.Chrome('~/danwaterfield/documents/github/webscraping/Selenium/ChromeDriver')  # Optional argument, if not specified will search path.
driver.get('http://www.google.com/xhtml');
time.sleep(5) # Let the user actually see something!
search_box = driver.find_element_by_name('q')
search_box.send_keys('ChromeDriver')
search_box.submit()
time.sleep(5) # Let the user actually see something!
driver.quit()