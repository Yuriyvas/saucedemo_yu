import allure
import pytest
# import time
from allure_commons.types import AttachmentType
from pages.page_headless import driver


class TestPageSearch:
    def setup_method(self):
        self.driver = driver

    # def teardown(self):
    #     self.driver.quit()

    @allure.feature('Open pages')
    @allure.story('Открывает страницу "google.com"')
    def test_google_search(self):
        self.driver.get('https://google.com')
        with allure.step('делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.title == 'Google'

    @allure.feature('Open pages')
    @allure.story('Открывает страницу "https://www.saucedemo.com/')
    def test_yandex_search(self):
        self.driver.get('https://www.saucedemo.com/')
        with allure.step('делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.title == 'Swag Labs'

    @allure.feature('Open pages')
    @allure.story('Открывает страницу "mail.ru"')
    @pytest.mark.xfail
    def test_mail_search(self):
        self.driver.get('https://mail.ru')
        with allure.step('делаем скриншот'):
            allure.attach(self.driver.get_screenshot_as_png(), name="Screenshot", attachment_type=AttachmentType.PNG)
        assert self.driver.title == 'Mail.ru'
