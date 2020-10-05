import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities


class TestTestHome():

    def setup_class(self):
        # self.driver = webdriver.Chrome()
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4444/wd/hub',desired_capabilities=DesiredCapabilities.CHROME)
        self.driver.implicitly_wait(10)
        self.driver.get("https://testerhome.com/")

    def test_mstc2019(self):
        self.driver.find_element_by_partial_link_text("MTSC 2020 深圳站").click()
        self.driver.find_element_by_xpath('//*[@data-toggle="dropdown" and @class="btn btn-default"]').click()
        self.driver.find_element_by_partial_link_text("大型3D图形渲染质量保障实践").click()

    def test_execute_script(self):
        self.driver.maximize_window()
        raw = self.driver.execute_script("return JSON.stringify(window.performance)")
        print(json.dumps(json.loads(raw), indent=4))

    def teardown_class(self):
        # time.sleep(5)
        self.driver.quit()