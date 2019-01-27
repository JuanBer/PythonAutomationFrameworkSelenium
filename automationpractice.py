import time
from selenium import webdriver

driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://automationpractice.com/index.php')
time.sleep(2)
search_box = driver.find_element_by_id('search_query_top')
search_btn = driver.find_element_by_name('submit_search')
search_box.send_keys('blouse')
search_btn.click()
time.sleep(2)
driver.quit()
