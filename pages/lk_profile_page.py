# -*- coding: utf-8 -*-
from .base_page import BasePage
from .locators import LkProfilePageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium import webdriver


class LkProfilePage(BasePage):
    def check_user2_email(self):
        current_email = self.browser.find_element(*LkProfilePageLocators.CHECK_EMAIL).text
        assert current_email == "dayafob606@riv3r.net", "Текущий e-mail не равен \'dayafob606@riv3r.net\'"

    def success_change_profile_data(self):
        self.browser.find_element(*LkProfilePageLocators.FIELD_NAME).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.browser.find_element(*LkProfilePageLocators.FIELD_NAME).send_keys("first name")
        self.browser.find_element(*LkProfilePageLocators.FIELD_LAST_NAME).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.browser.find_element(*LkProfilePageLocators.FIELD_LAST_NAME).send_keys("last name")
        self.browser.find_element(*LkProfilePageLocators.FIELD_MIDDLE_NAME).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.browser.find_element(*LkProfilePageLocators.FIELD_MIDDLE_NAME).send_keys("middle name")
        self.browser.find_element(*LkProfilePageLocators.FIELD_DATE_OF_BIRTH).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.browser.find_element(*LkProfilePageLocators.FIELD_DATE_OF_BIRTH).send_keys("11112001")
        self.browser.find_element(*LkProfilePageLocators.FIELD_PHONE).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.browser.find_element(*LkProfilePageLocators.FIELD_PHONE).send_keys("9261234455")
        self.browser.find_element(*LkProfilePageLocators.BUTTON_SAVE).click()
        self.browser.refresh()
        enter_disabled = self.browser.find_element(*LkProfilePageLocators.BUTTON_SAVE)
        assert enter_disabled.get_attribute("disabled"), "Значение кнопки \'Вход\' не равно \'disabled\'"

    def check_update_user2_name(self):
        self.find_element2(LkProfilePageLocators.PROFILE_DROPDOWN).click()
        user2_name = self.find_element1(LkProfilePageLocators.ACTUAL_NAME_PROFILE_DROPDOWN).text
        assert user2_name == "first name!", "Текущее имя не \'first name\'"

    def input_empty_data_in_fields(self):
        self.browser.find_element(*LkProfilePageLocators.FIELD_NAME).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.browser.find_element(*LkProfilePageLocators.FIELD_LAST_NAME).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.browser.find_element(*LkProfilePageLocators.FIELD_MIDDLE_NAME).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.browser.find_element(*LkProfilePageLocators.FIELD_DATE_OF_BIRTH).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.browser.find_element(*LkProfilePageLocators.FIELD_PHONE).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.browser.find_element(*LkProfilePageLocators.BUTTON_SAVE).click()

    def check_error_empty_field(self):
        error_empty_name = self.browser.find_element(*LkProfilePageLocators.ERROR_EMPTY_NAME).text
        assert error_empty_name == "Заполните поле", "нет сообщения \'Заполните поле\'"
        error_empty_last_name = self.browser.find_element(*LkProfilePageLocators.ERROR_EMPTY_LAST_NAME).text
        assert error_empty_last_name == "Заполните поле", "нет сообщения \'Заполните поле\'"
        error_birth = self.browser.find_element(*LkProfilePageLocators.ERROR_BIRTH).text
        assert error_birth == "Введите правильную дату", "нет сообщения \'Введите правильную дату\'"
        error_phone = self.browser.find_element(*LkProfilePageLocators.ERROR_PHONE).text
        assert error_phone == "Введите правильный номер", "нет сообщения \'Введите правильный номер\'"

    def profile_input_long_name(self):
        to_long_name = "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii"
        self.browser.find_element(*LkProfilePageLocators.FIELD_NAME).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.browser.find_element(*LkProfilePageLocators.FIELD_NAME).send_keys(f"{to_long_name}")
        self.browser.find_element(*LkProfilePageLocators.FIELD_LAST_NAME).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.browser.find_element(*LkProfilePageLocators.FIELD_LAST_NAME).send_keys(f"{to_long_name}")
        self.browser.find_element(*LkProfilePageLocators.FIELD_MIDDLE_NAME).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.browser.find_element(*LkProfilePageLocators.FIELD_MIDDLE_NAME).send_keys(f"{to_long_name}")
        self.browser.find_element(*LkProfilePageLocators.BUTTON_SAVE).click()

    def check_error_long_name(self):
        error_long_name = self.browser.find_element(*LkProfilePageLocators.ERROR_LONG_NAME).text
        assert error_long_name == "не более 40 символов.", "нет сообщения \'не более 40 символов.\'"
        error_long_last_name = self.browser.find_element(*LkProfilePageLocators.ERROR_LONG_LAST_NAME).text
        assert error_long_last_name == "не более 40 символов.", "нет сообщения \'не более 40 символов.\'"
        error_long_middle_name = self.browser.find_element(*LkProfilePageLocators.ERROR_LONG_MIDDLE_NAME).text
        assert error_long_middle_name == "не более 40 символов.", "нет сообщения \'не более 40 символов.\'"

    def profile_input_wrong_data_phone(self, phone):
        self.browser.find_element(*LkProfilePageLocators.FIELD_PHONE).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.browser.find_element(*LkProfilePageLocators.FIELD_PHONE).send_keys(f"{phone}")
        self.browser.find_element(*LkProfilePageLocators.BUTTON_SAVE).click()
        wrong_phone = self.browser.find_element(*LkProfilePageLocators.ERROR_SAVE).text
        assert wrong_phone == "Произошла ошибка,\nпопробуйте позже", "нет сообщения с серверной ошибкой"

    def profile_input_wrong_date_of_birth(self, date_of_birth):
        self.browser.find_element(*LkProfilePageLocators.FIELD_DATE_OF_BIRTH).send_keys(Keys.CONTROL, "a", Keys.DELETE)
        self.browser.find_element(*LkProfilePageLocators.FIELD_DATE_OF_BIRTH).send_keys(f"{date_of_birth}")
        self.browser.find_element(*LkProfilePageLocators.BUTTON_SAVE).click()
        error_birth = self.browser.find_element(*LkProfilePageLocators.ERROR_BIRTH).text
        assert error_birth == "Введите правильную дату", "нет сообщения \'Введите правильную дату\'"
