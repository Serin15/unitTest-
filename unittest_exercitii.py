import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class LoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("https://the-internet.herokuapp.com")
        self.driver.maximize_window()
        self.driver.find_element(By.LINK_TEXT, "Form Authentication").click()


    def tearDown(self):
        self.driver.quit()

    def test_url_curent(self):
        expected_result = "https://the-internet.herokuapp.com/login"
        actual_result = self.driver.current_url

        #assert expected_result == actual_result, "Unexpected URL"
        self.assertEqual(expected_result, actual_result, "Unexpected URL")

    def test_page_title(self):
        expected_title = "The Internet"
        actual_title = self.driver.title

        self.assertEqual(expected_title,actual_title, "Unexpected title")


    def test_login_form_title(self):
        expected_login_page = "Login Page"
        element = self.driver.find_element(By.XPATH, "//h2")
        actual_text = element.text

        self.assertEqual(expected_login_page,actual_text,"Unexpected text")


    def test_invalid_login(self):
       self.driver.find_element(By.CLASS_NAME, "radius").click()
       error_element = self.driver.find_element(By.ID, "flash")

       self.assertTrue(error_element.is_displayed())
       expected_text = "Your username is invalid!"
       actual_text = error_element.text

       self.assertIn(expected_text,actual_text, "Text not present!")

    def test_successful_login(self):
        self.driver.find_element(By.ID, "username").send_keys("tomsmith")
        self.driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        self.driver.find_element(By.CLASS_NAME, "radius").click()

        successful_message = self.driver.find_element(By.ID, "flash")
        self.assertIn("You logged into a secure area!", successful_message.text)



    def test_close_login_error(self):
        self.driver.find_element(By.CLASS_NAME, "radius").click()
        error_element = self.driver.find_element(By.ID, "flash")

        self.assertTrue(error_element.is_displayed())

        self.driver.find_element(By.CLASS_NAME, "close").click()
        time.sleep(1)

        assert self.is_absent((By.ID, "flash"))

    def is_absent(self, locator) -> bool:
        list_elements = self.driver.find_elements(*locator)

        return len(list_elements) == 0

