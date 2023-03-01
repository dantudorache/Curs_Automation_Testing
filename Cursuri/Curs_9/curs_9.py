# Locators in Selenium : ID, name, class, partial link text, link text, CSS, xPath
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time


# # ID
# chrom_page = webdriver.Chrome()     # .Chrome este clasa din pachetul selenium
# chrom_page.get('https://the-internet.herokuapp.com/login')      # accesarea paginii HTML
#
#
# chrom_page.find_element(By.ID, 'username').send_keys('dan')
# time.sleep(5)
#
# chrom_page.find_element(By.ID, 'password').send_keys('123456')
#
#
# chrom_page.find_element(By.TAG_NAME, 'button').click()
# time.sleep(5)
#
# chrom_page.find_element(By.LINK_TEXT, 'Elemental Selenium').click()
# time.sleep(5)
#
#
# chrom_page.quit()  # inchide toata instanta browser ului
# #chrom_page.close()   # inchide un singur tab cel activ

###########################################################################################


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

test = webdriver.Chrome()
test.get('https://the-internet.herokuapp.com/login')

test.find_element(By.TAG_NAME, 'form')

test.find_element(By.CSS_SELECTOR, "form >div [type = 'text']").send_keys('dan')
time.sleep(5)

# test.find_element(By.CSS_SELECTOR, "form >div [type = 'text']").clear()
test.find_element(By.CSS_SELECTOR, "form >div [type = 'text']").send_keys(Keys.CONTROL + 'a')

test.find_element(By.CSS_SELECTOR, "form >div:nth-of-type(1) input").send_keys('adela')
time.sleep(3)
test.find_element(By.CSS_SELECTOR, "form>div:last-of-type input").send_keys('password')
test.find_element(By.CSS_SELECTOR, "form >div [type = 'text']").send_keys(Keys.CONTROL + 'a')
time.sleep(3)
test.find_element(By.CSS_SELECTOR, "form>div:first-of-type input").send_keys('455')
time.sleep(10)

test.quit()


















































































