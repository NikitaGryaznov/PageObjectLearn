# -*- coding: utf-8 -*-
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def browser():
    browser_options = Options()
    browser_options.headless = bool(os.getenv('CI'))
    browser_options.add_experimental_option('prefs', {'intl.accept_languages': 'en'})
    browser = webdriver.Chrome(options=browser_options)
    browser.implicitly_wait(5)
    browser.maximize_window()
    yield browser
    browser.quit()
