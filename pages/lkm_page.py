# -*- coding: utf-8 -*-
from .base_page import BasePage
from .locators import LkmPageLocators


class LkmPage(BasePage):
    def log_in_to_lkm_merchant(self, login, password):
        self.browser.find_element(*LkmPageLocators.LKM_AUTH_FIELD_LOGIN).send_keys(f"{login}")
        self.browser.find_element(*LkmPageLocators.LKM_AUTH_FIELD_PASSWORD).send_keys(f"{password}")
        self.browser.find_element(*LkmPageLocators.LKM_AUTH_BUTTON_LOG_IN).click()

    def current_email_merchant(self):
        email_merchant = self.browser.find_element(*LkmPageLocators.LKM_CURRENT_EMAIL_MERCHANT1_PROFILE_DROPDOWN).text
        assert email_merchant == "fimej10248@mailres.net", "Неверное имя пользователя"

    def log_out_to_lkm_merchant(self):
        self.browser.find_element(*LkmPageLocators.LKM_CURRENT_EMAIL_MERCHANT1_PROFILE_DROPDOWN).click()
        self.browser.find_element(*LkmPageLocators.LKM_BUTTON_LOG_OUT).click()
        check_log_out = self.browser.find_element(*LkmPageLocators.TABLABEL_MODULE_AUTHORIZATION).text
        assert check_log_out == "Авторизация", "Нет вкладки \'Авторизация\'"

    def log_in_to_lkm_with_empty_fields(self):
        self.browser.find_element(*LkmPageLocators.LKM_AUTH_CHECKBOX_REMEMBER).click()
        self.browser.find_element(*LkmPageLocators.LKM_AUTH_BUTTON_LOG_IN).click()

    def lkm_auth_error_missing_username_or_password(self):
        error_message1 = self.browser.find_element(*LkmPageLocators.LKM_AUTH_ERROR).text
        assert error_message1 == "Missing username or password", "Нет сообщения \'Missing username or password\'"

    def lkm_auth_error_username_or_password_is_incorrect(self):
        error_message2 = self.browser.find_element(*LkmPageLocators.LKM_AUTH_ERROR).text
        error_message2_1 = "Нет сообщения \'username or password is incorrect.\'"
        assert error_message2 == "username or password is incorrect.", f"{error_message2_1}"
