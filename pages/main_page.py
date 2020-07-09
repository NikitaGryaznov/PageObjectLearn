# -*- coding: utf-8 -*-
from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def geo_accept_moscow(self):
        self.browser.find_element(*MainPageLocators.BUTTON_YES).click()
        current_city = self.browser.find_element(*MainPageLocators.ACTUAL_CITY)
        assert current_city.text == "Москва", "Текущий город - не Москва"

    def authorization_lk_user1(self):
        self.browser.find_element(*MainPageLocators.ICON_LK).click()
        self.browser.find_element(*MainPageLocators.BUTTON_LOG_IN).click()
        self.browser.find_element(*MainPageLocators.ENTRANCE_FIELD_EMAIL).send_keys("test@robokassa.ru")
        self.browser.find_element(*MainPageLocators.ENTRANCE_FIELD_PASSWORD).send_keys("test-password")
        self.browser.find_element(*MainPageLocators.BUTTON_ENTER).click()

    def current_name_user1(self):
        name_user1 = self.browser.find_element(*MainPageLocators.ACTUAL_NAME_DROPDOWN_LOGGED).text
        # Имя пользователя должно быть - Ivan2
        assert name_user1 == "Мы рады вас видеть,\nIvan2!", "Неверное имя пользователя"

    def authorization_lk_user2(self):
        self.browser.find_element(*MainPageLocators.ICON_LK).click()
        self.browser.find_element(*MainPageLocators.BUTTON_LOG_IN).click()
        self.browser.find_element(*MainPageLocators.ENTRANCE_FIELD_EMAIL).send_keys("dayafob606@riv3r.net")
        self.browser.find_element(*MainPageLocators.ENTRANCE_FIELD_PASSWORD).send_keys("testpassword")
        self.browser.find_element(*MainPageLocators.BUTTON_ENTER).click()

    def get_to_profile_section(self):
        self.browser.find_element(*MainPageLocators.HEADER_DROPDOWN_LOGGED_PROFILE).click()

    def authorization_errors_empty_fields(self):
        self.browser.find_element(*MainPageLocators.ICON_LK).click()
        self.browser.find_element(*MainPageLocators.BUTTON_LOG_IN).click()
        self.browser.find_element(*MainPageLocators.BUTTON_ENTER).click()
        error_mail = self.browser.find_element(*MainPageLocators.ERROR_EMAIL_FIELD).text
        assert error_mail == "Введите электронную почту", "Нет сообщения \'Введите электронную почту\'"
        error_password = self.browser.find_element(*MainPageLocators.ERROR_PASSWORD_FIELD).text
        assert error_password == "Введите пароль", "Нет сообщения \'Введите пароль\'"
        enter_disabled = self.browser.find_element(*MainPageLocators.BUTTON_ENTER)
        assert enter_disabled.get_attribute("disabled"), "Значение кнопки \'Вход\' не равно \'disabled\'"

    def authorization_input_wrong_mail(self, email):
        self.browser.find_element(*MainPageLocators.ICON_LK).click()
        self.browser.find_element(*MainPageLocators.BUTTON_LOG_IN).click()
        self.browser.find_element(*MainPageLocators.ENTRANCE_FIELD_EMAIL).send_keys(f"{email}")
        self.browser.find_element(*MainPageLocators.ENTRANCE_FIELD_PASSWORD).send_keys("test-password")
        self.browser.find_element(*MainPageLocators.BUTTON_ENTER).click()

    def error_user_not_found(self):
        user_not_found = self.browser.find_element(*MainPageLocators.ERROR_USER_NOT_FOUND).text
        assert user_not_found == "User not found.", "Нет сообщения \'User not found.\'"

    def error_wrong_mail(self):
        wrong_mail = self.browser.find_element(*MainPageLocators.ERROR_SET_ACTUAL_EMAIL).text
        wrong_mail2 = "Нет сообщения \'Введите настоящий адрес электроной почты\'"
        assert wrong_mail == "Введите настоящий адрес электроной почты", f"{wrong_mail2}"
        enter_disabled = self.browser.find_element(*MainPageLocators.BUTTON_ENTER)
        assert enter_disabled.get_attribute("disabled"), "Значение кнопки \'Вход\' не равно \'disabled\'"

    def authorization_input_wrong_password(self, password):
        self.browser.find_element(*MainPageLocators.ICON_LK).click()
        self.browser.find_element(*MainPageLocators.BUTTON_LOG_IN).click()
        self.browser.find_element(*MainPageLocators.ENTRANCE_FIELD_EMAIL).send_keys("test@robokassa.ru")
        self.browser.find_element(*MainPageLocators.ENTRANCE_FIELD_PASSWORD).send_keys(f"{password}")
        self.browser.find_element(*MainPageLocators.BUTTON_ENTER).click()

    def error_wrong_password(self):
        wrong_password = self.browser.find_element(*MainPageLocators.ERROR_INVALID_USER_OR_PASSWORD).text
        wrong_password2 = "Нет сообщения \'Invalid username or password.\'"
        assert wrong_password == "Invalid username or password.", f"{wrong_password2}"

    def authorization_input_only_email(self):
        self.browser.find_element(*MainPageLocators.ICON_LK).click()
        self.browser.find_element(*MainPageLocators.BUTTON_LOG_IN).click()
        self.browser.find_element(*MainPageLocators.ENTRANCE_FIELD_EMAIL).send_keys("test@robokassa.ru")
        self.browser.find_element(*MainPageLocators.BUTTON_ENTER).click()

    def error_input_only_email(self):
        input_only_email = self.browser.find_element(*MainPageLocators.ERROR_PASSWORD_FIELD).text
        assert input_only_email == "Введите пароль", "Нет сообщения \'Введите пароль\'"
        enter_disabled = self.browser.find_element(*MainPageLocators.BUTTON_ENTER)
        assert enter_disabled.get_attribute("disabled"), "Значение кнопки \'Вход\' не равно \'disabled\'"

    def authorization_input_only_password(self):
        self.browser.find_element(*MainPageLocators.ICON_LK).click()
        self.browser.find_element(*MainPageLocators.BUTTON_LOG_IN).click()
        self.browser.find_element(*MainPageLocators.ENTRANCE_FIELD_PASSWORD).send_keys("test-password")
        self.browser.find_element(*MainPageLocators.BUTTON_ENTER).click()

    def error_input_only_password(self):
        input_only_password = self.browser.find_element(*MainPageLocators.ERROR_EMAIL_FIELD).text
        assert input_only_password == "Введите электронную почту", "Нет сообщения \'Введите электронную почту\'"
        enter_disabled = self.browser.find_element(*MainPageLocators.BUTTON_ENTER)
        assert enter_disabled.get_attribute("disabled"), "Значение кнопки \'Вход\' не равно \'disabled\'"

    """def registration_input_data(self):
        self.browser.find_element(*RegistrationPageLocators.ICON_LK).click()
        self.browser.find_element(*RegistrationPageLocators.BUTTON_REGISTRATION).click()
        mail1, mail2 = self.check_secmail_page()
        self.browser.find_element(*RegistrationPageLocators.REG_FIELD_EMAIL).send_keys(mail1, "@", mail2)
        self.browser.find_element(*RegistrationPageLocators.REG_FIELD_FIRST_NAME).send_keys("тест1")
        self.browser.find_element(*RegistrationPageLocators.REG_FIELD_LAST_NAME).send_keys("тест2")
        self.browser.find_element(*RegistrationPageLocators.BUTTON_GO_TO_REG).click()
        popup_reg = self.browser.find_element(*RegistrationPageLocators.POPUP_REG)
        assert popup_reg is not None, "Нет модального окна \'Регистрация\'"""
