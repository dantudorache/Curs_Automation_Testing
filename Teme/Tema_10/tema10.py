import time
import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.select import Select


class Firefox_Test(TestCase):
    WEB_FORM = (By.XPATH, '/html/body/div/div/li[14]/a')
    FIRST_NAME = (By.XPATH,'//*[@id="first-name"]')
    LAST_NAME = (By.XPATH, '//*[@id="last-name"]')
    JOB_TITLE = (By.XPATH, '//*[@id="job-title"]')
    HS_BUTTON = (By.XPATH, '//*[@id="radio-button-1"]')
    GENDER_BUTTON = (By.XPATH, '//*[@id="checkbox-1"]')
    DATA_BUTTON = (By.XPATH, '//*[@id="datepicker"]')
    SUBMIT_BUTTON = (By.XPATH, '/html/body/div/form/div/div[8]/a')
    ALERT = (By.XPATH,'/html/body/div/div')

    def setUp(self) -> None:
        self.firefox = webdriver.Firefox()
        self.firefox.get("https://formy-project.herokuapp.com/")
        self.firefox.maximize_window()
        self.firefox.implicitly_wait(2)
        self.firefox.find_element(*self.WEB_FORM).click()

    def tearDown(self) -> None:
        self.firefox.quit()

    # @unittest.skip
    def test_date_personale(self):
        self.firefox.find_element(*self.FIRST_NAME).send_keys('DAN')
        time.sleep(2)
        self.firefox.find_element(*self.LAST_NAME).send_keys('TUDORACHE')
        time.sleep(2)
        self.firefox.find_element(*self.JOB_TITLE).send_keys('Tester Automat')
        time.sleep(2)

    # @unittest.skip
    def test_select(self):
        self.firefox.find_element(*self.HS_BUTTON).click()
        time.sleep(2)
        self.firefox.find_element(*self.GENDER_BUTTON).click()
        time.sleep(2)

    def test_dropdown(self):
        dropdown = self.firefox.find_element(By.XPATH, '//*[@id="select-menu"]')
        dd = Select(dropdown)
        dd.select_by_visible_text('2-4')
        time.sleep(2)

    def test_data(self):
        self.firefox.find_element(*self.DATA_BUTTON).send_keys('05/10/1991')
        time.sleep(2)
        self.firefox.find_element(*self.SUBMIT_BUTTON).click()
        time.sleep(3)




























































