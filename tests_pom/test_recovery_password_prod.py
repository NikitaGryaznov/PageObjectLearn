# -*- coding: utf-8 -*-
import pytest
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage
import time

"""
Запуск теста - pytest -s -v -m smoke test_recovery_password_prod.py
Запуск одного теста - pytest -s -v -m smoke -k test_recovery_password_success
Запуск всех Smoke тестов - pytest -s -v -m smoke .
"""


@pytest.mark.smoke
@pytest.mark.parametrize('name1', ['тест1'])
@pytest.mark.parametrize('name2', ['тест2'])
@pytest.mark.parametrize('password', ['testpassword'])
@pytest.mark.parametrize('newpassword', ['newpassword'])
def test_recovery_password_success(browser, name1, name2, password, newpassword):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    window0 = browser.window_handles[0]
    page_reg = RegistrationPage(browser, link)
    page_reg.go_to_sec_mail()
    window1 = browser.window_handles[1]
    browser.switch_to.window(window1)
    page_reg.get_email_adress()
    browser.switch_to.window(window0)
    page_reg.go_to_robomarket_reg(name1, name2)
    page_reg.check_popup_registration()
    browser.switch_to.window(window1)
    page_reg.letter_create_password()
    page_reg.letter_create_password_click_to_link()
    window2 = browser.window_handles[2]
    browser.switch_to.window(window2)
    page_reg.input_password(password)
    page_reg.check_username()
    page_reg.logout_from_lk()
    page_reg.forget_password()
    page_reg.input_field_recovery_password_email()
    browser.switch_to.window(window1)
    page_reg.letter_recovery_password()
    page_reg.open_link_recovery_password()
    window3 = browser.window_handles[3]
    browser.switch_to.window(window3)
    page_reg.input_recovery_password(newpassword)
    page_reg.confirm_recovery_password()
    page_reg.login_lk_new_password()
    page_reg.check_username()


@pytest.mark.smoke
@pytest.mark.parametrize('email', [''])
def test_recovery_password_input_empty_email(browser, email):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page_reg = RegistrationPage(browser, link)
    page_reg.forget_password()
    page_reg.recovery_password_input_email(email)
    page_reg.error_recovery_password_empty_email()


@pytest.mark.smoke
@pytest.mark.parametrize('email', ['@qq.qq', 'qwe@qwe', 'qwerty', 'qwe.rty', '.qq@qq.qq.', 'qw@qw.#$qw',
                                   'qq.@.qq.qq', 'qq..qq@qq..qq.qq', 'qq qq@qq qq.qq', 'qw@qw.12qw'])
def test_recovery_password_input_wrong_email(browser, email):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page_reg = RegistrationPage(browser, link)
    page_reg.forget_password()
    page_reg.recovery_password_input_email(email)
    page_reg.error_recovery_wrong_mail()


@pytest.mark.smoke
@pytest.mark.parametrize('email', ['q@q.q', 'q@q.qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq',
                                   '123wrongmail@qwerty.zz'])
def test_recovery_password_email_not_found(browser, email):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page_reg = RegistrationPage(browser, link)
    page_reg.forget_password()
    page_reg.recovery_password_input_email(email)
    page_reg.error_recovery_password_email_not_found()


@pytest.mark.smoke
@pytest.mark.parametrize('name1', ['тест1'])
@pytest.mark.parametrize('name2', ['тест2'])
@pytest.mark.parametrize('password', ['testpassword'])
@pytest.mark.parametrize('newpassword', [''])
def test_recovery_password_input_empty_newpassword(browser, name1, name2, password, newpassword):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    window0 = browser.window_handles[0]
    page_reg = RegistrationPage(browser, link)
    page_reg.go_to_sec_mail()
    window1 = browser.window_handles[1]
    browser.switch_to.window(window1)
    page_reg.get_email_adress()
    browser.switch_to.window(window0)
    page_reg.go_to_robomarket_reg(name1, name2)
    page_reg.check_popup_registration()
    browser.switch_to.window(window1)
    page_reg.letter_create_password()
    page_reg.letter_create_password_click_to_link()
    window2 = browser.window_handles[2]
    browser.switch_to.window(window2)
    page_reg.input_password(password)
    page_reg.check_username()
    page_reg.logout_from_lk()
    page_reg.forget_password()
    page_reg.input_field_recovery_password_email()
    browser.switch_to.window(window1)
    page_reg.letter_recovery_password()
    page_reg.open_link_recovery_password()
    window3 = browser.window_handles[3]
    browser.switch_to.window(window3)
    page_reg.input_recovery_password(newpassword)
    page_reg.error_empty_newpassword()
