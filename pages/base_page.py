# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver


class BasePage:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def by_xpath(self, browser: webdriver.Chrome, xpath: str) -> WebElement:
        return browser.find_element_by_xpath(xpath)

    def by_css_selector(self, browser: webdriver.Chrome, css_selector: str) -> WebElement:
        return browser.find_element_by_css_selector(css_selector)

    def find_el(self, locator):
        return self.browser.find_element(locator)

    def find_element1(self, locator, time=70):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator),
                                                       message=f"Can't find element by locator {locator}")

    def find_element2(self, locator, time=70):
        return WebDriverWait(self.browser, time).until(EC.element_to_be_clickable(locator),
                                                       message=f"Can't find element by locator {locator}")

    def go_to_site(self):
        self.browser.get(self.url)

    """def go_to_email_generation_page(self):
        print("qaz")
        self.browser.execute_script("window.open('https://www.1secmail.com/')")"""

    """def check_secmail_page(self):
        print(self.__dict__)
        #check_mail = self.browser.find_element(*SecMailPageLocators.CHECK_MAIL)
        #assert check_mail is not None, "Нет кнопки \'Check mail\'"
        mail1 = self.find_element1(SecMailPageLocators.MAIL_PATH1).get_attribute("value")
        mail2 = self.find_element1(SecMailPageLocators.MAIL_PATH2).get_attribute("value")
        return mail1, mail2"""
