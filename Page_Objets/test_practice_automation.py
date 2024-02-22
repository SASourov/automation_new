import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from Utilities.config import UserInfo

from Page_Objets.practice_test_automation import LogIn, NavigateMenu


class Test_001_Login:
    def test_invalid_user(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(UserInfo.url)
        self.lp = LogIn(self.driver)
        self.lp.set_username(UserInfo.invalid_username)
        self.lp.set_password(UserInfo.valid_password)
        self.lp.click_submit_button()
        time.sleep(2)

        expected_text = self.driver.find_element(By.ID, "error").text
        if expected_text == "Your username is invalid!":
            assert True
            print("Your Expected Title is : ", expected_text)

        else:
            assert False

        print("1st test case done....\n")
        self.driver.quit()


class Test_002_Login:
    def test_invalid_password(self, setup):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(UserInfo.url)
        self.lp = LogIn(self.driver)
        self.lp.set_username(UserInfo.valid_username)
        self.lp.set_password(UserInfo.invalid_password)
        self.lp.click_submit_button()
        time.sleep(2)

        expected_text = self.driver.find_element(By.ID, "error").text
        if expected_text == "Your password is invalid!":
            assert True
            print("Your Expected Title is : ", expected_text)

        else:
            assert False

        print("2nd test case done....\n")
        self.driver.close()


class Test_003_Login:
    def test_valid_data(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(UserInfo.url)
        self.lp = LogIn(self.driver)
        self.lp.set_username(UserInfo.valid_username)
        self.lp.set_password(UserInfo.valid_password)
        self.lp.click_submit_button()
        time.sleep(3)

        expected_text = self.driver.find_element(By.XPATH, "//p[@class='has-text-align-center']//strong[1]").text
        if expected_text == "Congratulations student. You successfully logged in!":
            assert True
            print("Your Expected Text: ", expected_text)

        else:
            assert False

        print("3rd test case done........ \n")
        self.driver.quit()


class Test_004_Navigation:
    def test_navigate_menu(self, setup):
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(UserInfo.url)
        self.lp = LogIn(self.driver)
        self.lp.set_username(UserInfo.valid_username)
        self.lp.set_password(UserInfo.valid_password)
        self.lp.click_submit_button()
        self.nm = NavigateMenu(self.driver)
        self.nm.click_home_link()
        self.nm.click_practice_link()
        self.nm.click_courses_link()
        self.nm.click_blog_link()
        self.nm.click_contact_link()

        expected_title = self.driver.title
        if expected_title == "Contact | Practice Test Automation | Selenium WebDriver":
            assert True
            print("Your Expected Title is : ", expected_title)

        else:
            assert True

        print("4th test case done......")
        self.driver.quit()
