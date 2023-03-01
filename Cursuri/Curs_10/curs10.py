# Folosirea librariei unitest
# Metoda de setup => pasi care se fac inainte de a executa testul in sine
# 1. instantierea unui obiect
# 2. maximise

# Metoda tear-down => toate activitatile care trebuie sa fie dupa test, ex: inchiderea browser ului

# toate metodele de test trebuie sa aiba ca si prefix "test_"
# se ruleaza testele in mod normal, din terminal sau click drepta si run

# import unittest #importa tot modulul. aici clasa mosteneste din unittest.TestCases
# sau "from unittest import testcases" in acest caz clasa mosteneste direct din TestCases

import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# crearea unui test

class Alerts(TestCase):
    ALERT_BUTTON = (By.XPATH, '//*[text()="Click for JS Alert"]')
    CONFIRM_BUTTON = (By.XPATH, '//*[text()="Click for JS Confirm"]')
    PROMPT_BUTTON = (By.XPATH, '//*[text()="Click for JS Prompt"]')
    ALERT_MSG = (By.ID, "result")


    # definirea metodei de setup
    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)

    # definirea metodei de tearDown
    def tearDown(self) -> None:
        self.chrome.quit()

    def test_alert_accept(self):
        self.chrome.find_element(*self.ALERT_BUTTON).click()
        js_alert = self.chrome.switch_to.alert
        js_alert.accept()  # built in method care accepta alerta e.g. da click pe buton
        actual_alert_msg = self.chrome.find_element(*self.ALERT_MSG).text
        expected_alert_msg = 'You successfully clicked an alert'
        assert actual_alert_msg == expected_alert_msg, f'error: {expected_alert_msg}, actual {self.ALERT_MSG}'
        # modalitate de a valida

    def test_confirm_accept(self):
        self.chrome.find_element(*self.CONFIRM_BUTTON).click()
        js_confirm = self.chrome.switch_to.alert
        js_confirm.accept()
        actual_confirm_msg = self.chrome.find_element(*self.ALERT_MSG).text
        expected_confirm_msg = 'You clicked: OK'
        assert actual_confirm_msg == expected_confirm_msg, f'error: {expected_confirm_msg}, actual {actual_confirm_msg}'

    def test_confirm_cancel(self):
            self.chrome.find_element(*self.CONFIRM_BUTTON).click()
            js_confirm = self.chrome.switch_to.alert
            js_confirm.dismiss()
            actual_confirm_msg = self.chrome.find_element(*self.ALERT_MSG).text
            expected_confirm_msg = 'You clicked: Cancel'
            assert actual_confirm_msg == expected_confirm_msg, f'error: {expected_confirm_msg}, actual {actual_confirm_msg}'

    def test_no_text_accept(self):
            self.chrome.find_element(*self.PROMPT_BUTTON).click()
            js_prompt = self.chrome.switch_to.alert
            js_prompt.accept()
            actual_prompt_msg = self.chrome.find_element(*self.ALERT_MSG).text
            expected_prompt_msg = 'You entered:'
            assert actual_prompt_msg == expected_prompt_msg, f'error: {expected_prompt_msg}, actual {actual_prompt_msg}'

    def test_no_text_cancel(self):
            self.chrome.find_element(*self.PROMPT_BUTTON).click()
            js_prompt = self.chrome.switch_to.alert
            js_prompt.dismiss()
            actual_prompt_msg = self.chrome.find_element(*self.ALERT_MSG).text
            expected_prompt_msg = 'You entered: null'
            assert actual_prompt_msg == expected_prompt_msg, f'error: {expected_prompt_msg}, actual {actual_prompt_msg}'

    def test_text_accept(self):
            self.chrome.find_element(*self.PROMPT_BUTTON).click()
            js_prompt = self.chrome.switch_to.alert
            js_prompt.send_keys('Hello')
            js_prompt.accept()
            actual_prompt_msg = self.chrome.find_element(*self.ALERT_MSG).text
            expected_prompt_msg = 'You entered: Hello'
            assert actual_prompt_msg == expected_prompt_msg, f'error: {expected_prompt_msg}, actual {actual_prompt_msg}'



























