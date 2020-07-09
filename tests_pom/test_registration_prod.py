# -*- coding: utf-8 -*-
import pytest
from pages.main_page import MainPage
from pages.registration_page import RegistrationPage

"""
Запуск теста - pytest -s -v -m smoke test_registration_prod.py
Запуск одного теста - pytest -s -v -m smoke -k test_registration_success
Запуск всех Smoke тестов - pytest -s -v -m smoke .
"""


@pytest.mark.smoke
@pytest.mark.parametrize('name1', ['тест1'])
@pytest.mark.parametrize('name2', ['тест2'])
@pytest.mark.parametrize('password', ['testpassword'])
def test_registration_success(browser, name1, name2, password):
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
    browser.switch_to.window(window1)
    page_reg.letter_registration_success()
    browser.switch_to.default_content()


@pytest.mark.smoke
def test_registration_empty_input_field(browser):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page_reg = RegistrationPage(browser, link)
    page_reg.registration_empty_input_field()


@pytest.mark.smoke
@pytest.mark.parametrize('email', ['@qq.qq', 'qwe@qwe', 'qwerty', 'qwe.rty', '.qq@qq.qq.', 'qw@qw.#$qw',
                                   'qq.@.qq.qq', 'qq..qq@qq..qq.qq', 'qq qq@qq qq.qq', 'qw@qw.12qw'])
def test_registration_input_wrong_mail(browser, email):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page_reg = RegistrationPage(browser, link)
    page_reg.registration_input_mail(email)
    page_reg.error_wrong_mail()


@pytest.mark.smoke
@pytest.mark.parametrize('email', ['q@q.q', 'q@q.qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq',
                                   '123wrongmail@qwerty.zz'])
def test_registration_input_not_well_formed_mail(browser, email):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page_reg = RegistrationPage(browser, link)
    page_reg.registration_input_mail(email)
    page_reg.error_not_well_formed_mail()


@pytest.mark.xfail  # bug RM-620
@pytest.mark.smoke
@pytest.mark.parametrize('name1', ['iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii'])
@pytest.mark.parametrize('name2', ['iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii'])
def test_registration_input_too_long_name(browser, name1, name2):
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
    page_reg.error_to_long_name()


@pytest.mark.smoke
@pytest.mark.parametrize('email', ['test@robokassa.ru'])
def test_registration_email_already_exist(browser, email):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page_reg = RegistrationPage(browser, link)
    page_reg.registration_input_mail(email)
    page_reg.error_email_already_exist()


@pytest.mark.smoke
@pytest.mark.parametrize('name1', ['тест1'])
@pytest.mark.parametrize('name2', ['тест2'])
@pytest.mark.parametrize('password', [''])
def test_registration_input_empty_password(browser, name1, name2, password):
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
    browser.switch_to.window(window1)
    page_reg.letter_create_password()
    page_reg.letter_create_password_click_to_link()
    window2 = browser.window_handles[2]
    browser.switch_to.window(window2)
    page_reg.input_password(password)
    page_reg.error_empty_password()


@pytest.mark.smoke
@pytest.mark.parametrize('name1', ['тест1'])
@pytest.mark.parametrize('name2', ['тест2'])
@pytest.mark.parametrize('password', ['123qwe', ' '])
def test_registration_input_short_password(browser, name1, name2, password):
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
    browser.switch_to.window(window1)
    page_reg.letter_create_password()
    page_reg.letter_create_password_click_to_link()
    window2 = browser.window_handles[2]
    browser.switch_to.window(window2)
    page_reg.input_password(password)
    page_reg.error_too_short_password()


@pytest.mark.smoke
@pytest.mark.parametrize('name1', ['тест1'])
@pytest.mark.parametrize('name2', ['тест2'])
@pytest.mark.parametrize('password', ['12345678'])
def test_registration_input_password_without_a_letter(browser, name1, name2, password):
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
    browser.switch_to.window(window1)
    page_reg.letter_create_password()
    page_reg.letter_create_password_click_to_link()
    window2 = browser.window_handles[2]
    browser.switch_to.window(window2)
    page_reg.input_password(password)
    page_reg.error_password_without_a_letter()


@pytest.mark.smoke
@pytest.mark.parametrize('name1', ['тест1'])
@pytest.mark.parametrize('name2', ['тест2'])
def test_registration_input_different_password(browser, name1, name2):
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
    browser.switch_to.window(window1)
    page_reg.letter_create_password()
    page_reg.letter_create_password_click_to_link()
    window2 = browser.window_handles[2]
    browser.switch_to.window(window2)
    page_reg.input_different_password()
    page_reg.error_different_password()
