from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# instance of Options class allows
# us to configure Headless Chrome
options = Options()
options.add_argument('--headless')

# this parameter tells Chrome that
# it should be run without UI (Headless)
# options.headless = True

# initializing webdriver for Chrome with our options
driver = webdriver.Chrome(options=options)

# getting GeekForGeeks webpage
driver.get('https://www.geeksforgeeks.org')

# assert driver.title == ('GeeksforGeeks | A computer science portal for geeks')


# We can also get some information
# about page in browser.
# So let's output webpage title into
# terminal to be sure that the browser
# is actually running.
print(driver.title)
driver.close()
# close browser after our manipulations

