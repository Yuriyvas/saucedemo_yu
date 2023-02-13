import pages.login_page.login_page
import pages.login_page.login_page_locators
import conf
import time
import allure
from allure_commons.types import AttachmentType
# from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.options import Options


options = Options()
options.add_argument('--headless')
options.headless = True
driver = webdriver.Chrome(options=options)

driver = WebDriver()

# options = Options()
# options.add_argument("start-maximized")
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
# driver.get("https://www.google.com")

# my first selenium test
# driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
# service = Service(executable_path=ChromeDriverManager().install())
# driver = webdriver.Chrome(service=service)
# driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

driver.get(conf.URL)


def test_login_page():
    driver.get(conf.URL)
    assert conf.URL


def test_title():
    title_from_site = driver.title
    assert title_from_site == conf.TITLE


def test_login_form():
    input_user_name = driver.find_element(By.ID, 'user-name')
    input_user_name.send_keys('standard_user')
    time.sleep(5)
    with allure.step('Вводим логин и' + ' ' + 'делаем скриншот'):
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    input_user_password = driver.find_element(By.ID, 'password')
    input_user_password.send_keys('secret_sauce')
    time.sleep(5)
    with allure.step('Вводим пароль и' + ' ' + 'делаем скриншот'):
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    input_login_button = driver.find_element(By.ID, 'login-button')
    input_login_button.click()
    time.sleep(5)

    with allure.step('Жмём на кнопку "LOGIN" и' + ' ' + 'делаем скриншот'):
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'We are reached another site'
