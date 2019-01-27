import time
import unittest
from selenium import webdriver


class automationPractice(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome('chromedriver.exe')
        self.driver.get('http://automationpractice.com/index.php')
        time.sleep(2)

    def test_VerifySearchTextBox(self):
        search_box = self.driver.find_element_by_id("search_query_top")
        text = search_box.get_attribute("placeholder")
        self.assertEqual(text,'Search','They are different')

    def test_BestSellersExist(self):
        bestseller_link = self.driver.find_element_by_class_name('blockbestsellers')
        text = bestseller_link.text
        self.assertTrue(bestseller_link.is_displayed(),'It is not displayed')
        self.assertEqual(text.lower(),'Best Sellers'.lower(),'Wrong text')

    def tearDown(self):
        self.driver.quit()
