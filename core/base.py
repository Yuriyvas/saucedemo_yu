import pages.login_page.login_page
import pages.login_page.login_page_locators
import conf
import time
import allure
from allure_commons.types import AttachmentType

from pages.login_page import login_page_locators
from pages.page_headless import driver
from selenium.webdriver.common.by import By
driver.get(conf.URL)



