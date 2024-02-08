from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest
import datetime



class TestReg(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def reg_main(self, link):
        self.browser.get(link)
        first_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block > .first_class > .first ")
        first_name.send_keys("Ivan")
        last_name = self.browser.find_element(By.CSS_SELECTOR, ".first_block > .second_class > .second")
        last_name.send_keys("Ivanov")
        last_name = self.browser.find_element(By.CSS_SELECTOR, ".third_class > .third")
        last_name.send_keys("q@q.ru")
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        welcome_text_elt = self.browser.find_element(By.TAG_NAME, "h1")
        return welcome_text_elt.text

    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        welcome_text = self.reg_main(link)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "link1")

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        welcome_text = self.reg_main(link)
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "link2")

    def tearDown(self):
        self.browser.quit()

# if __name__ == "__main__":
#     unittest.main()






