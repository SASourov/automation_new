from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import random
import string

from Page_Objets.new_practices import SignUpButton

random_num = random.randint(00, 99)


class Test_001_LunchBrowser:
    def test_homepage_visible(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()
        self.driver.get('http://automationexercise.com')
        actual_title = self.driver.title
        if actual_title == "Automation Exercise":
            print("home page is visible successfully")
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
        self.sup.set_name("Abul")
        self.sup.set_mail("abul" + str(random_num) + "@mail.com")
        self.sup.click_signup_btn()
        self.sup.select_name_title()
        self.sup.set_password("abc123@")
        self.sup.select_newsletter()

        set_b_date = Select(self.driver.find_element(By.ID, "days"))
        set_b_date.select_by_value("5")

        set_b_month = Select(self.driver.find_element(By.ID, "months"))
        set_b_month.select_by_value("5")

        set_b_year = Select(self.driver.find_element(By.ID, "years"))
        set_b_year.select_by_value("1999")

        self.sup.set_first_name("Abul" + str(random_num))
        self.sup.set_last_name("Kalam")
        self.sup.set_address_1("Dhaka, Bangladesh")
        self.sup.set_address_2("Same as address1")
        select_country = Select(self.driver.find_element(By.ID, "country"))
        select_country.select_by_value("Australia")
        self.sup.set_state("Canada's state")
        self.sup.set_city("Dhaka")
        self.sup.set_zip_code("56562")
        self.sup.set_mobile_number("01723969323")
        self.sup.click_create_account()

        expected_text = self.driver.find_element(By.XPATH, "//b[text()='Account Created!']").text
        actual_text = "ACCOUNT CREATED!"

        if expected_text == actual_text:
            print("Your account is created", actual_text)

        else:
            print("ACCOUNT IS NOT CREATED!")

        self.sup.click_continue_button()
        expected_text = self.driver.find_element(By.XPATH,
                                                 "//header[@id='header']/div[1]/div[1]/div[1]/div[2]/div[1]/ul[1]/li[10]/a[1]").text
        if expected_text == "Logged in as Shakil":
            print("Test Passed")

        else:
            print("Test Failed")

        self.sup.click_delete_account()
        expected_text = self.driver.find_element(By.XPATH, "//b[text()='Account Deleted!']")
        if expected_text == "ACCOUNT DELETED!":
            print("Test Passed")

        else:
            print("Test Failed")
            self.driver.save_screenshot(r"D:\basic_automation\Screen_Shot\test" + str(random_num) + ".png")
        self.sup.click_continue_btn()
