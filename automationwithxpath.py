import time
from selenium import webdriver
driver = webdriver.Chrome('chromedriver.exe')
driver.get('http://newtours.demoaut.com/')
time.sleep(5)
username_box = driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form[@name='home']/table/tbody/tr[4]/td/table/tbody/tr[2]/td[2]/input[@name='userName']")
password_box = driver.find_element_by_xpath("/html/body/div/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[3]/form[@name='home']/table/tbody/tr[4]/td/table/tbody/tr[3]/td[2]/input[@name='password']")
username_box.send_keys('test')
password_box.send_keys('test')
time.sleep(5)
drver.quit()


