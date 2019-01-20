import time
from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://newtours.demoaut.com/')
time.sleep(5)
username_box = driver.find_element_by_name('userName')
password_box = driver.find_element_by_name('password')
signin_btn = driver.find_element_by_name('login')

username_box.send_keys('test')
password_box.send_keys('test')
signin_btn.click()
time.sleep(5)
driver.quit()