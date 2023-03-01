# Ex 1

import time
import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Login(TestCase):
    FORM_AUTH = (By.XPATH, '//*[@id="content"]/ul/li[21]/a')
    H2_ELEMENT = (By.XPATH, '//h2')
    LOGIN_BUTTON = (By.XPATH, '//*[@id="login"]/button/i')
    HREF_LINK = (By.XPATH, '//*[@id="page-footer"]/div/div/a')
    ERROR_LOGIN = (By.XPATH, '//*[@id="flash"]')
    USERNAME = (By.XPATH, '//*[@id="username"]')
    PASSWORD = (By.XPATH, '//*[@id="password"]')
    ERROR_MSG = (By.XPATH, '//*[@id="flash"]')
    CANCEL_BUTTON = (By.XPATH, '//*[@id="flash"]/a')
    LABEL_LIST = (By.XPATH, '//label')
    LOGOUT_BUTTON = (By.XPATH, '//*[@id="content"]/div/a')


    def setUp(self) -> None:
        self.chrome = webdriver.Chrome()
        self.chrome.get("https://the-internet.herokuapp.com/")
        self.chrome.maximize_window()
        self.chrome.implicitly_wait(2)
        self.chrome.find_element(*self.FORM_AUTH).click()

    def tearDown(self) -> None:
        self.chrome.quit()
    # @unittest.skip
    def test_1(self):
        actual_url = self.chrome.current_url
        new_url = 'https://the-internet.herokuapp.com/login'
        assert actual_url == new_url, f'Noul URL nu este corect!'
        time.sleep(3)

    # @unittest.skip
    def test_2(self):
        actual_title = self.chrome.title
        new_title = 'The Internet'
        assert actual_title == new_title, f'Expected title is: {new_title} and teh actual title is {actual_title}'

    # @unittest.skip
    def test_3(self):
        actual_text = self.chrome.find_element(* self.H2_ELEMENT).text
        expected = 'Login Page'
        assert actual_text == expected, f'Textul nu este cel asteptat'

    # @unittest.skip
    def test_4(self):
        display_button = self.chrome.find_element(*self.LOGIN_BUTTON)
        self.assertTrue(display_button.is_displayed(),'Login button is not displayed!')

    # @unittest.skip
    def test_5(self):
        actual_link = self.chrome.find_element(*self.HREF_LINK).get_attribute('href')
        assert actual_link == 'http://elementalselenium.com/', 'Link-ul nu este corect!'

    # @unittest.skip
    def test_6(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        error = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.ERROR_MSG))
        self.assertTrue(error.is_displayed(), 'Error not displayed')

        print('error displayed')

    # @unittest.skip
    def test_7(self):
        self.chrome.find_element(*self.USERNAME).send_keys('alabala')
        self.chrome.find_element(*self.PASSWORD).send_keys('1111')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = self.chrome.find_element(*self.ERROR_MSG).text
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')

    # @unittest.skip
    def test_8(self):
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(3)
        self.chrome.find_element(*self.CANCEL_BUTTON).click()
        time.sleep(3)
        try:
            self.chrome.find_element(*self.ERROR_MSG)
        except NoSuchElementException:
            print("Error not displayed")

    def test_11(self):
        self.chrome.find_element(*self.USERNAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        time.sleep(3)
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()
        actual_url = self.chrome.current_url
        new_url = 'https://the-internet.herokuapp.com/login'
        assert actual_url == new_url, f'Noul URL nu este corect!'
        time.sleep(3)



























































