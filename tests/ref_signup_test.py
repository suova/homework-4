import os
import unittest
from selenium.webdriver import DesiredCapabilities, Remote

from pages.mainpage import MainPage


class RefSignUpTest(unittest.TestCase):

    def setUp(self):
        browser = os.environ.get('BROWSER', 'CHROME')

        self.driver = Remote(
            command_executor='http://127.0.0.1:4444/wd/hub',
            desired_capabilities=getattr(DesiredCapabilities, browser).copy()
        )

    def tearDown(self):
        self.driver.quit()

    def test(self):
        driver = self.driver

        mainpage = MainPage(driver)
        mainpage.open()
        mainsteps = mainpage.steps
        mainsteps.button_signin()
        driver.switch_to.frame(driver.find_element_by_css_selector('[class="ag-popup__frame__layout__iframe"]'))
        mainsteps.ref_signup()

        assert "No results found." not in driver.page_source