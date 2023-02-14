import conf
import selenium.webdriver.chrome
from selenium.webdriver.common.by import By
from pages.page_headless import driver
driver.get(conf.URL)

input_user_name = driver.find_element(By.ID, 'user-name')
input_user_password = driver.find_element(By.ID, 'password')
input_login_button = driver.find_element(By.ID, 'login-button')