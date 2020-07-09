# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from pages.main_page import MainPage

"""
Запуск теста - pytest -s -v -m smoke test_auth_prod.py
Запуск одного теста - pytest -s -v -m smoke -k test_authorization_success
Запуск всех Smoke тестов - pytest -s -v -m smoke .
"""


@pytest.mark.smoke
def test_authorization_success(browser):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page.authorization_lk_user1()
    page.current_name_user1()


@pytest.mark.smoke
def test_authorization_empty_input_field(browser):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page.authorization_errors_empty_fields()


@pytest.mark.smoke
@pytest.mark.parametrize('email', ['q@q.q', 'q@q.qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq',
                                   '123wrongmail@qwerty.zz'])
def test_authorization_user_not_found(browser, email):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page.authorization_input_wrong_mail(email)
    page.error_user_not_found()


@pytest.mark.smoke
@pytest.mark.parametrize('email', ['@qq.qq', 'qwe@qwe', 'qwerty', 'qwe.rty', '.qq@qq.qq.', 'qw@qw.#$qw',
                                   'qq.@.qq.qq', 'qq..qq@qq..qq.qq', 'qq qq@qq qq.qq', 'qw@qw.12qw'])
def test_authorization_input_wrong_mail(browser, email):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page.authorization_input_wrong_mail(email)
    page.error_wrong_mail()


@pytest.mark.smoke
@pytest.mark.parametrize('passwords', [' ', 'wrong-password'])
def test_authorization_input_wrong_password(browser, passwords):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page.authorization_input_wrong_password(passwords)
    page.error_wrong_password()


@pytest.mark.smoke
def test_authorization_input_only_email(browser):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page.authorization_input_only_email()
    page.error_input_only_email()


@pytest.mark.smoke
def test_authorization_input_only_password(browser):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page.authorization_input_only_password()
    page.error_input_only_password()
