import selenium
from selenium.webdriver import chrome
from selenium.webdriver.chrome.options import Options
opts = Options()
opts.set_headless()
assert opts.headless  # Operating in headless mode
browser = chrome(opts)
browser.get('https://duckduckgo.com')