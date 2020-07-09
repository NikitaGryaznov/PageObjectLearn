# -*- coding: utf-8 -*-
import pytest
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from pages.main_page import MainPage
from pages.lk_profile_page import LkProfilePage

"""
Сгенерированный temp-mail для автотеста
email: dayafob606@riv3r.net
password: testpassword
Запуск теста - pytest -s -v -m smoke test_check_profile_prod.py
Запуск одного теста - pytest -s -v -m smoke -k test_check_profile_email
Запуск всех Smoke тестов - pytest -s -v -m smoke .
"""


@pytest.mark.smoke
def test_check_profile_email(browser):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page.authorization_lk_user2()
    page.get_to_profile_section()
    page_lk = LkProfilePage(browser, link)
    page_lk.check_user2_email()


@pytest.mark.smoke
def test_success_change_profile_data(browser):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page.authorization_lk_user2()
    page.get_to_profile_section()
    page_lk = LkProfilePage(browser, link)
    page_lk.success_change_profile_data()
    page_lk.check_update_user2_name()


@pytest.mark.smoke
def test_profile_input_empty_fields(browser):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page.authorization_lk_user2()
    page.get_to_profile_section()
    page_lk = LkProfilePage(browser, link)
    page_lk.input_empty_data_in_fields()
    page_lk.check_error_empty_field()


@pytest.mark.smoke
@pytest.mark.xfail
def test_profile_input_long_name(browser):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page.authorization_lk_user2()
    page.get_to_profile_section()
    page_lk = LkProfilePage(browser, link)
    page_lk.profile_input_long_name()
    page_lk.check_error_long_name()


@pytest.mark.smoke
@pytest.mark.parametrize('phone', ['6001112233', '1234567890'])
def test_profile_input_wrong_data_phone(browser, phone):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page.authorization_lk_user2()
    page.get_to_profile_section()
    page_lk = LkProfilePage(browser, link)
    page_lk.profile_input_wrong_data_phone(phone)


@pytest.mark.smoke
@pytest.mark.parametrize('date_of_birth', ['10301999', '20011800', '00000000', '11111111', '11112100'])
def test_profile_input_wrong_date_of_birth(browser, date_of_birth):
    link = "https://robo.market/"
    page = MainPage(browser, link)
    page.go_to_site()
    page.geo_accept_moscow()
    page.authorization_lk_user2()
    page.get_to_profile_section()
    page_lk = LkProfilePage(browser, link)
    page_lk.profile_input_wrong_date_of_birth(date_of_birth)
