# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from pages.main_page import MainPage
from pages.lkm_page import LkmPage

"""
Запуск теста - pytest -s -v -m smoke test_auth_kozy_lkm.py
Запуск одного теста - pytest -s -v -m smoke -k test_log_in_to_lkm_success
Запуск всех Smoke тестов - pytest -s -v -m smoke .
"""


@pytest.mark.smoke
@pytest.mark.parametrize('login', ['fimej10248@mailres.net'])
@pytest.mark.parametrize('password', ['oUqlAeNN'])
def test_log_in_to_lkm_success(browser, login, password):
    link = "https://cozy.market/merchant/login"
    page = MainPage(browser, link)
    page.go_to_site()
    page_auth_lkm = LkmPage(browser, link)
    page_auth_lkm.log_in_to_lkm_merchant(login, password)
    page_auth_lkm.current_email_merchant()


@pytest.mark.smoke
@pytest.mark.parametrize('login', ['fimej10248@mailres.net'])
@pytest.mark.parametrize('password', ['oUqlAeNN'])
def test_log_out_to_lkm_success(browser, login, password):
    link = "https://cozy.market/merchant/login"
    page = MainPage(browser, link)
    page.go_to_site()
    page_auth_lkm = LkmPage(browser, link)
    page_auth_lkm.log_in_to_lkm_merchant(login, password)
    page_auth_lkm.current_email_merchant()
    page_auth_lkm.log_out_to_lkm_merchant()


@pytest.mark.smoke
def test_log_in_to_lkm_with_empty_fields(browser):
    link = "https://cozy.market/merchant/login"
    page = MainPage(browser, link)
    page.go_to_site()
    page_auth_lkm = LkmPage(browser, link)
    page_auth_lkm.log_in_to_lkm_with_empty_fields()
    page_auth_lkm.lkm_auth_error_missing_username_or_password()


@pytest.mark.smoke
@pytest.mark.parametrize('login', ['q@q.q', 'q@q.qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq',
                                   '123wrongmail@qwerty.zz', '@qq.qq', ' '])
@pytest.mark.parametrize('password', ['oUqlAeNN'])
def test_log_in_to_lkm_input_wrong_login(browser, login, password):
    link = "https://cozy.market/merchant/login"
    page = MainPage(browser, link)
    page.go_to_site()
    page_auth_lkm = LkmPage(browser, link)
    page_auth_lkm.log_in_to_lkm_merchant(login, password)
    page_auth_lkm.lkm_auth_error_username_or_password_is_incorrect()


@pytest.mark.smoke
@pytest.mark.parametrize('login', ['fimej10248@mailres.net'])
@pytest.mark.parametrize('password', ['wrong-password', ' '])
def test_log_in_to_lkm_input_wrong_password(browser, login, password):
    link = "https://cozy.market/merchant/login"
    page = MainPage(browser, link)
    page.go_to_site()
    page_auth_lkm = LkmPage(browser, link)
    page_auth_lkm.log_in_to_lkm_merchant(login, password)
    page_auth_lkm.lkm_auth_error_username_or_password_is_incorrect()
