import pages.login_page.login_page
import pages.login_page.login_page_locators
import conf
import time
import allure
from allure_commons.types import AttachmentType
from core import base
from pages.login_page import login_page_locators
from pages.page_headless import driver
from selenium.webdriver.common.by import By

driver.get(conf.URL)


def test_login_page():
    driver.get(conf.URL)

    with allure.step('Открываем и' + ' ' + 'делаем скриншот'):
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    assert conf.URL


def test_title():
    title_from_site = driver.title
    with allure.step('Проверяем TITLE и' + ' ' + 'делаем скриншот'):
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    assert title_from_site == conf.TITLE


def test_login_form():
    login_page_locators.input_user_name.send_keys('standard_user')
    with allure.step('Вводим логин и' + ' ' + 'делаем скриншот'):
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)

    login_page_locators.input_user_password.send_keys('secret_sauce')

    with allure.step('Вводим пароль и' + ' ' + 'делаем скриншот'):
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    login_page_locators.input_login_button.click()

    with allure.step('Жмём на кнопку "LOGIN" и' + ' ' + 'делаем скриншот'):
        allure.attach(driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'We are reached another site'
