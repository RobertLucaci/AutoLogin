import unittest
from selenium import webdriver


class TheInternetLogin(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='/home/robertlucaci/PycharmProjects/Automation and Testing/geckodriver')
        self.driver.maximize_window()

    def test_login(self):
        driver = self.driver
        driver.get('http://the-internet.herokuapp.com/login')
        assert 'The Internet' in driver.title
        username = driver.find_element_by_id('username')
        username.clear()
        username.send_keys('tomsmith')
        password = driver.find_element_by_id('password')
        password.clear()
        password.send_keys('SuperSecretPassword!')
        button = driver.find_element_by_class_name('fa-sign-in')
        assert 'Login' in button.text
        button.click()

    def tearDown(self):
        self.driver.close()


if __name__ == '__main__':
    unittest.main()
