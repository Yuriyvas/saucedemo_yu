
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
# options.headless = True
options.add_argument('-headless')
driver = webdriver.Firefox(options=options)

