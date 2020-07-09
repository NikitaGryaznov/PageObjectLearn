# -*- coding: utf-8 -*-
from .base_page import BasePage
from .locators import RegistrationPageLocators
from .locators import MainPageLocators


class RegistrationPage(BasePage):
    mail1 = ""
    mail2 = ""

    def go_to_sec_mail(self):
        self.browser.execute_script("window.open('https://www.1secmail.com/')")

    def get_email_adress(self):
        check_mail = self.browser.find_element(*RegistrationPageLocators.CHECK_MAIL)
        assert check_mail is not None, "Нет кнопки \'Check mail\'"
        self.mail1 = self.find_element1(RegistrationPageLocators.MAIL_PATH1).get_attribute("value")
        self.mail2 = self.find_element1(RegistrationPageLocators.MAIL_PATH2).get_attribute("value")

    def go_to_robomarket_reg(self, name1, name2):
        self.browser.find_element(*RegistrationPageLocators.ICON_LK).click()
        self.browser.find_element(*RegistrationPageLocators.BUTTON_REGISTRATION).click()
        value_mail = self.browser.find_element(*RegistrationPageLocators.REG_FIELD_EMAIL)
        value_mail.send_keys(self.mail1, "@", self.mail2)
        self.browser.find_element(*RegistrationPageLocators.REG_FIELD_FIRST_NAME).send_keys(f"{name1}")
        self.browser.find_element(*RegistrationPageLocators.REG_FIELD_LAST_NAME).send_keys(f"{name2}")
        self.browser.find_element(*RegistrationPageLocators.BUTTON_GO_TO_REG).click()

    def check_popup_registration(self):
        popup_reg = self.browser.find_element(*RegistrationPageLocators.POPUP_REG)
        assert popup_reg is not None, "Нет модального окна \'Регистрация\'"

    def letter_create_password(self):
        self.find_element1(RegistrationPageLocators.LETTER_CONFIRM_EMAIL).click()
        self.browser.switch_to.frame(self.browser.find_element(*RegistrationPageLocators.SWITCH_TO_IFRAME_LETTER_LINK))
        already_done = self.browser.find_element(*RegistrationPageLocators.LETTER_CHECK)
        assert already_done is not None, "Нет письма с созданием пароля"
        assert already_done.text == "Почти готово!", "!= Почти готово!"

    def letter_create_password_click_to_link(self):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);",
                                    self.browser.find_element(*RegistrationPageLocators.LETTER_GO_TO_LINK))
        link_password = self.find_element1(RegistrationPageLocators.LETTER_LINK_CREATE_PASSWORD).get_attribute("href")
        self.browser.switch_to.default_content()
        secmail_massage_details = self.find_element1(RegistrationPageLocators.SECMAIL_MESSAGE_DETAILS)
        assert secmail_massage_details.text == "Message details", "!= Message details"
        self.browser.execute_script("window.open(arguments[0],'_blank');", link_password)

    def input_password(self, password):
        self.find_element1(RegistrationPageLocators.INPUT_PASSWORD1).send_keys(f"{password}")
        self.find_element1(RegistrationPageLocators.INPUT_PASSWORD2).send_keys(f"{password}")
        self.browser.find_element(*RegistrationPageLocators.BUTTON_PASSWORD).click()

    def input_different_password(self):
        self.find_element1(RegistrationPageLocators.INPUT_PASSWORD1).send_keys("qwerty123")
        self.find_element1(RegistrationPageLocators.INPUT_PASSWORD2).send_keys("asdfgh123")
        self.browser.find_element(*RegistrationPageLocators.BUTTON_PASSWORD).click()

    def error_different_password(self):
        disabled = "Значение кнопки \'Зарегистрироваться\' не равно \'disabled\'"
        assert self.find_element1(RegistrationPageLocators.BUTTON_PASSWORD).get_attribute("disabled"), f"{disabled}"
        different_password = self.browser.find_element(*RegistrationPageLocators.ERROR_DIFFERENT_PASSWORD)
        assert different_password.text == "Пароли должны совпадать", "Нет сообщения \'Пароли должны совпадать\'"

    def check_username(self):
        dropdown_login = self.browser.find_element(*RegistrationPageLocators.DROPDOWN_LOGIN)
        assert dropdown_login is not None, "Нет меню ЛК"
        assert dropdown_login.text == "Мы рады вас видеть,\nтест1!", "Неверное имя пользователя"

    def error_empty_password(self):
        disabled = "Значение кнопки \'Зарегистрироваться\' не равно \'disabled\'"
        assert self.find_element1(RegistrationPageLocators.BUTTON_PASSWORD).get_attribute("disabled"), f"{disabled}"
        empty_password1 = self.browser.find_element(*RegistrationPageLocators.ERROR_EMPTY_PASSWORD1)
        assert empty_password1.text == "Введите пароль", "Нет сообщения \'Введите пароль\'"
        empty_password2 = self.browser.find_element(*RegistrationPageLocators.ERROR_EMPTY_PASSWORD2)
        assert empty_password2.text == "Введите пароль еще раз", "Нет сообщения \'Введите пароль еще раз\'"

    def error_too_short_password(self):
        disabled = "Значение кнопки \'Зарегистрироваться\' не равно \'disabled\'"
        assert self.find_element1(RegistrationPageLocators.BUTTON_PASSWORD).get_attribute("disabled"), f"{disabled}"
        too_short_password1 = self.browser.find_element(*RegistrationPageLocators.ERROR_TOO_SHORT_PASSWORD1)
        assert too_short_password1.text == "Слишком короткий пароль", "Нет сообщения \'Слишком короткий пароль\'"
        too_short_password2 = self.browser.find_element(*RegistrationPageLocators.ERROR_TOO_SHORT_PASSWORD2)
        assert too_short_password2.text == "Слишком короткий пароль", "Нет сообщения \'Слишком короткий пароль\'"

    def error_password_without_a_letter(self):
        disabled = "Значение кнопки \'Зарегистрироваться\' не равно \'disabled\'"
        assert self.find_element1(RegistrationPageLocators.BUTTON_PASSWORD).get_attribute("disabled"), f"{disabled}"
        error = "Пароль должен содержать не менее 8 символов и как минимум одну латинскую букву"
        without_a_letter1 = self.browser.find_element(*RegistrationPageLocators.ERROR_PASSWORD_WITHOUT_LETTER1)
        assert without_a_letter1.text == f"{error}", f"Нет сообщения \'{error}\'"
        without_a_letter2 = self.browser.find_element(*RegistrationPageLocators.ERROR_PASSWORD_WITHOUT_LETTER2)
        assert without_a_letter2.text == f"{error}", f"Нет сообщения \'{error}\'"

    def letter_registration_success(self):
        self.browser.find_element(*RegistrationPageLocators.SECMAIL_GO_BACK).click()
        self.find_element1(RegistrationPageLocators.LETTER_REGISTRATION_DONE).click()
        self.browser.switch_to.frame(self.browser.find_element(*RegistrationPageLocators.SWITCH_TO_IFRAME_LETTER_LINK))
        registration_success = self.browser.find_element(*RegistrationPageLocators.LETTER_REGISTRATION_SUCCESS)
        assert registration_success is not None, "Нет письма \'Отлично - регистрация прошла успешно!\'"

    def registration_empty_input_field(self):
        self.browser.find_element(*RegistrationPageLocators.ICON_LK).click()
        self.browser.find_element(*RegistrationPageLocators.BUTTON_REGISTRATION).click()
        self.browser.find_element(*RegistrationPageLocators.BUTTON_GO_TO_REG).click()
        error_empty_email = self.browser.find_element(*RegistrationPageLocators.ERROR_EMPTY_EMAIL)
        assert error_empty_email is not None, "Нет сообщения \'Введите электронную почту\'"
        error_empty_first_name = self.browser.find_element(*RegistrationPageLocators.ERROR_EMPTY_FIRST_NAME)
        assert error_empty_first_name is not None, "Нет сообщения \'Введите имя\'"
        error_empty_last_name = self.browser.find_element(*RegistrationPageLocators.ERROR_EMPTY_LAST_NAME)
        assert error_empty_last_name is not None, "Нет сообщения \'Введите фамилию\'"
        disabled = "Значение кнопки \'Зарегистрироваться\' не равно \'disabled\'"
        assert self.find_element1(RegistrationPageLocators.BUTTON_GO_TO_REG).get_attribute("disabled"), f"{disabled}"

    def registration_input_mail(self, email):
        self.browser.find_element(*RegistrationPageLocators.ICON_LK).click()
        self.browser.find_element(*RegistrationPageLocators.BUTTON_REGISTRATION).click()
        self.browser.find_element(*RegistrationPageLocators.REG_FIELD_EMAIL).send_keys(f"{email}")
        self.browser.find_element(*RegistrationPageLocators.REG_FIELD_FIRST_NAME).send_keys("тест1")
        self.browser.find_element(*RegistrationPageLocators.REG_FIELD_LAST_NAME).send_keys("тест2")
        self.browser.find_element(*RegistrationPageLocators.BUTTON_GO_TO_REG).click()

    def error_wrong_mail(self):
        disabled = "Значение кнопки \'Зарегистрироваться\' не равно \'disabled\'"
        wrong_message = "Нет сообщения \'Введите настоящий адрес электроной почты\'"
        assert self.find_element1(RegistrationPageLocators.BUTTON_GO_TO_REG).get_attribute("disabled"), f"{disabled}"
        error_set_actual_email = self.browser.find_element(*RegistrationPageLocators.ERROR_SET_ACTUAL_EMAIL)
        assert error_set_actual_email.text == "Введите настоящий адрес электроной почты", f"{wrong_message}"

    def error_not_well_formed_mail(self):
        not_well_formed = self.browser.find_element(*RegistrationPageLocators.ERROR_NOT_WELL_FORMED_EMAIL)
        wrong_message = "Нет сообщения \'Not a well-formed email address.\'"
        assert not_well_formed.text == "Not a well-formed email address.", f"{wrong_message}"

    def error_to_long_name(self):
        disabled = "Значение кнопки \'Зарегистрироваться\' не равно \'disabled\'"
        assert self.find_element1(RegistrationPageLocators.BUTTON_GO_TO_REG).get_attribute("disabled"), f"{disabled}"

    def error_email_already_exist(self):
        already_exist = self.browser.find_element(*RegistrationPageLocators.ERROR_EMAIL_ALREADY_EXIST)
        assert already_exist is not None, "Other Error"
        assert already_exist.text == "Email already confirmed.", "Нет сообщения \'Email already confirmed.\'"

    def logout_from_lk(self):
        self.find_element1(RegistrationPageLocators.BUTTON_LOGOUT_LK).click()
        self.find_element1(RegistrationPageLocators.LOGO_ROBOMARKET).click()

    def forget_password(self):
        self.find_element2(RegistrationPageLocators.ICON_LK).click()
        self.find_element1(MainPageLocators.BUTTON_LOG_IN).click()
        self.find_element1(RegistrationPageLocators.BUTTON_FORGET_PASSWORD).click()
        password_recovery = self.browser.find_element(*RegistrationPageLocators.POPUP_PASSWORD_RECOVERY)
        assert password_recovery is not None, "Нет модального окна \'Восстановление пароля\'"

    def recovery_password_input_email(self, email):
        self.browser.find_element(*RegistrationPageLocators.RECOVERY_PASSWORD_FIELD_EMAIL).send_keys(f"{email}")
        self.find_element1(RegistrationPageLocators.BUTTON_CONFIRM_RECOVERY_PASSWORD).click()

    def error_recovery_wrong_mail(self):
        error = "Нет сообщения \'Введите настоящий адрес электроной почты\'"
        wrong_mail = self.browser.find_element(*RegistrationPageLocators.ERROR_SET_ACTUAL_EMAIL)
        assert wrong_mail.text == "Введите настоящий адрес электроной почты", f"{error}"
        disabled = self.find_element1(RegistrationPageLocators.BUTTON_DISABLED_CONFIRM_RECOVERY)
        assert disabled.get_attribute("disabled"), "Значение кнопки \'Зарегистрироваться\' не равно \'disabled\'"

    def error_recovery_password_empty_email(self):
        empty_mail = self.browser.find_element(*RegistrationPageLocators.ERROR_RECOVERY_PASSWORD_EMPTY_MAIL)
        assert empty_mail.text == "Заполните поле", "нет сообщения \'Заполните поле'\'"
        disabled = self.find_element1(RegistrationPageLocators.BUTTON_DISABLED_CONFIRM_RECOVERY)
        assert disabled.get_attribute("disabled"), "Значение кнопки \'Зарегистрироваться\' не равно \'disabled\'"

    def error_recovery_password_email_not_found(self):
        user_not_found = self.browser.find_element(*RegistrationPageLocators.ERROR_EMAIL_NOT_FOUND).text
        assert user_not_found == "E-mail not found.", "Нет сообщения \'E-mail not found.\'"

    def error_empty_newpassword(self):
        empty_newpassword = self.browser.find_element(*RegistrationPageLocators.BUTTON_CONFIRM_PASSWORD_DISABLED)
        assert empty_newpassword.get_attribute("disabled"), "Значение кнопки \'Подтвердить\' не равно \'disabled\'"
        empty_newpassword1 = self.browser.find_element(*RegistrationPageLocators.ERROR_EMPTY_PASSWORD1)
        assert empty_newpassword1.text == "Введите пароль", "Нет сообщения \'Введите пароль\'"
        empty_newpassword2 = self.browser.find_element(*RegistrationPageLocators.ERROR_EMPTY_PASSWORD2)
        assert empty_newpassword2.text == "Введите пароль еще раз", "Нет сообщения \'Введите пароль еще раз\'"

    def input_field_recovery_password_email(self):
        value_mail = self.browser.find_element(*RegistrationPageLocators.RECOVERY_PASSWORD_FIELD_EMAIL)
        value_mail.send_keys(self.mail1, "@", self.mail2)
        self.find_element1(RegistrationPageLocators.BUTTON_CONFIRM_RECOVERY_PASSWORD).click()
        button_recovery = self.browser.find_element(*RegistrationPageLocators.POPUP_PASSWORD_RECOVERY_SEND)
        assert button_recovery.get_attribute("disabled"), "Значение кнопки \'Подтвердить\' не равно \'disabled\'"
        self.find_element1(RegistrationPageLocators.POPUP_PASSWORD_RECOVERY_SEND_AGAIN).click()

    def letter_recovery_password(self):
        self.browser.find_element(*RegistrationPageLocators.SECMAIL_GO_BACK).click()
        self.browser.find_element(*RegistrationPageLocators.SECMAIL_REFRESH).click()
        self.find_element1(RegistrationPageLocators.LETTER_RECOVERY_PASSWORD).click()
        self.browser.switch_to.frame(self.browser.find_element(*RegistrationPageLocators.SWITCH_TO_IFRAME_LETTER_LINK))
        recovery = self.browser.find_element(*RegistrationPageLocators.LETTER_CHECK)
        assert recovery is not None, "Нет письма с востановлением пароля"
        assert recovery.text == "Востановление пароля", "!= Востановление пароля"

    def open_link_recovery_password(self):
        self.browser.execute_script("return arguments[0].scrollIntoView(true);",
                                    self.browser.find_element(*RegistrationPageLocators.LETTER_GO_TO_LINK))
        link_password = self.find_element1(RegistrationPageLocators.LETTER_LINK_CREATE_PASSWORD).get_attribute("href")
        self.browser.switch_to.default_content()
        secmail_massage_details = self.find_element1(RegistrationPageLocators.SECMAIL_MESSAGE_DETAILS)
        assert secmail_massage_details.text == "Message details", "!= Message details"
        self.browser.execute_script("window.open(arguments[0],'_blank');", link_password)

    def input_recovery_password(self, newpassword):
        password_recovery = self.browser.find_element(*RegistrationPageLocators.POPUP_PASSWORD_RECOVERY)
        assert password_recovery is not None, "Нет модального окна \'Восстановление пароля\'"
        self.find_element1(RegistrationPageLocators.INPUT_NEW_PASSWORD1).send_keys(f"{newpassword}")
        self.find_element1(RegistrationPageLocators.INPUT_NEW_PASSWORD2).send_keys(f"{newpassword}")
        self.find_element1(RegistrationPageLocators.BUTTON_CONFIRM_RECOVERY_PASSWORD).click()

    def confirm_recovery_password(self):
        success_recovery = self.browser.find_element(*RegistrationPageLocators.POPUP_PASS_REC_SUCCESS)
        assert success_recovery is not None, "Нет модального окна \'Пароль изменен\'"
        self.find_element1(RegistrationPageLocators.BUTTON_RECOVERY_GO_TO_CATALOG).click()

    def login_lk_new_password(self):
        self.find_element2(RegistrationPageLocators.ICON_LK).click()
        self.find_element1(MainPageLocators.BUTTON_LOG_IN).click()
        value_mail = self.browser.find_element(*MainPageLocators.ENTRANCE_FIELD_EMAIL)
        value_mail.send_keys(self.mail1, "@", self.mail2)
        self.find_element1(MainPageLocators.ENTRANCE_FIELD_PASSWORD).send_keys("newpassword")
        self.find_element1(MainPageLocators.BUTTON_ENTER).click()

    """def example_function(self):
        m1, m2 = self.get_email_adress()
        self.go_to_robomarket_reg(m1, m2)"""
