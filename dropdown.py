import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://newtours.demoaut.com/')
time.sleep(5)
register_lnk = driver.find_element_by_link_text('REGISTER')
register_lnk.click()
time.sleep(5)
country_dropdown = Select(driver.find_element_by_name('country'))
country_dropdown.select_by_value('8')
time.sleep(2)
country_dropdown.select_by_visible_text('BAHAMAS')
time.sleep(2)
country_dropdown.select_by_index(81)
time.sleep(2)
driver.quit()