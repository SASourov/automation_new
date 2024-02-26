import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random
import string

from Page_Objets.new_practices import SignUpButton, InvalidLogin, Logout

random_num = random.randint(000, 999)
phn_num = random.randint(0000000000, 99999999999)


class Test_001_LunchBrowser:
    def test_homepage_visible(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get('http://automationexercise.com')
        actual_title = self.driver.title
        if actual_title == "Automation Exercise":
            print("TC 001 is passed.\nHome page is visible successfully")
        else:
            print("Home page is not visible")
        self.driver.close()


class Test_002_ClickSignUpButton:
    def test_click_signup_button(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get('http://automationexercise.com')
        self.sup = SignUpButton(self.driver)
        self.sup.click_menu()
        self.sup.set_name("Abul Kashem")  #+ str(random_num)
        self.sup.set_mail("abul009@mail.com") #+ str(random_num) + "
        self.sup.click_signup_btn()
        time.sleep(3)
        self.sup.select_name_title()
        time.sleep(3)
        self.sup.set_password("abc123@")

        set_b_date = Select(self.driver.find_element(By.ID, "days"))
        set_b_date.select_by_value("5")

        set_b_month = Select(self.driver.find_element(By.ID, "months"))
        set_b_month.select_by_value("5")

        set_b_year = Select(self.driver.find_element(By.ID, "years"))
        set_b_year.select_by_value("1999")
        time.sleep(2)

        self.sup.select_newsletter()
        time.sleep(3)

        self.sup.set_first_name("Abul")  #+ str(random_num)
        self.sup.set_last_name("Kalam")
        self.sup.set_address_1("Dhaka, Bangladesh")
        self.sup.set_address_2("Same as address1")
        select_country = Select(self.driver.find_element(By.ID, "country"))
        select_country.select_by_value("Australia")
        self.sup.set_state("Canada's state")
        self.sup.set_city("Dhaka")
        self.sup.set_zip_code(str(random_num))
        self.sup.set_mobile_number(phn_num)
        time.sleep(2)
        self.sup.click_create_account()
        time.sleep(2)
        expected_text = self.driver.find_element(By.XPATH, "//b[text()='Account Created!']").text
        actual_text = "ACCOUNT CREATED!"
        if expected_text == actual_text:
            assert True
            print("YOUR IS ACCOUNT CREATED! \nYour expected text is: ", expected_text)
        else:
            print("ACCOUNT NOT CREATED!")

        self.sup.click_continue_button()
        actual_title = self.driver.title
        expected_title = "Automation Exercise"
        if actual_title == expected_title:
            assert True
            print("'Logged in as username' is visible")

        else:
            print("'Logged in as username' is not visible")

        self.sup.click_delete_account()
        expected_text = self.driver.find_element(By.XPATH, "//b[text()='Account Deleted!']")
        if expected_text == "ACCOUNT DELETED!":
            assert True
            print("ACCOUNT DELETED!")

        else:
            print("ACCOUNT IS NOT DELETED!")

        self.sup.click_continue_btn()
        actual_title = self.driver.title
        expected_title = "Automation Exercise"
        if actual_title == expected_title:
            assert True

            print("TC 002 is passed.\nYour expected title is: ", actual_title)
        else:
            print("TC 002 is failed")
        time.sleep(3)
        self.driver.close()


class Test_Case_003_Invalid_Login:
    def test_invalid_login(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get('http://automationexercise.com')
        self.invalidlogin = InvalidLogin(self.driver)
        self.invalidlogin.click_menu()
        self.invalidlogin.set_email("akil12@mailinator.com")
        self.invalidlogin.set_password("1222")
        self.invalidlogin.click_login_button()
        error_message = self.driver.find_element(By.XPATH, "//div[@class='login-form']//p[1]").text

        if error_message == "Your email or password is incorrect!":
            assert True
            print("TC 003 is passed.\nYour error message is: ", error_message)

        else:
            print("TC 003 is failed")
        self.driver.close()


class Test_Case_004_Logout:
    def test_logout(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get('http://automationexercise.com')
        self.logout = Logout(self.driver)
        self.logout.click_menu()
        self.logout.set_email("shakil12@mailinator.com")
        self.logout.set_password("111222")
        self.logout.click_login_button()
        time.sleep(3)
        self.logout.click_logout_button()
        indentify_text = self.driver.find_element(By.XPATH, "//h2[text()='Login to your account']").text

        if indentify_text == "Login to your account":
            print("TC 004 is passed. \nNavigate To Home Page")

        else:
            print("TC 004 is failed")

        self.driver.close()
