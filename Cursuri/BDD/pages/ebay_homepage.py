from selenium.webdriver.support.select import Select
from pages.base_page import Base_page
from selenium.webdriver.common.by import By

class Home_page(Base_page):
    SEARCH_TEXT_BOX = (By.ID, 'gh-ac')
    SEARCH_BUTTON = (By.ID, 'gh-btn')
    SEARCH_CATEGORIES = (By.ID,'gh-cat')
    ADVANCESD_SEARCH_LINK = (By.ID, 'gh-as-td')
    SEARCH_RESULTS = (By.XPATH,'//h1/span[@class="BOLD"][1]')

    def navigate_to_homepage(self):
        self.chrome.get('https://www.ebay.com/')

    def insert_search_value(self, product_name):
        self.chrome.find_element(*self.SEARCH_TEXT_BOX).send_keys(product_name)

    def choose_category(self, category_name):
        category_dropdown = Select(self.chrome.find_element(*self.SEARCH_CATEGORIES))
        category_dropdown.select_by_visible_text(category_name)

    def click_search_button(self):
        self.chrome.find_element(*self.SEARCH_BUTTON).click()

    def click_advanced_link(self):
        self.wait_and_click_element(*self.ADVANCESD_SEARCH_LINK)

    def check_search_results(self, nr_of_results):
        partial_results = self.chrome.find_element(*self.SEARCH_RESULTS).text
        result = partial_results.replace(",", "")
        assert int(result) >= int(nr_of_results), f'Error! Results are incorect. Expected: {nr_of_results}, Actual{result}'





