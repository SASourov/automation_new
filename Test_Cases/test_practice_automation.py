import pytest
from selenium import webdriver
from Page_Objets.practice_test_automation import LogIn, NavigateMenu, SubmitContact


class TestLogIn:
    valid_user_name = "student"
    invalid_user_name = "Student"

    valid_password = "Password123"
    invalid_password = "password123"

    url = "https://practicetestautomation.com/practice-test-login/"

    def test_valid_data(self, setup):
        self.driver = setup
        self.lp = LogIn(self.driver)
        self.lp.set_username("student")
        self.lp.set_password("Password")
        self.lp.click_login_button()
        self.nm = NavigateMenu(self.driver)
        self.nm.click_home_link()
        self.nm.click_practice_link()
        self.nm.click_courses_link()
        self.nm.click_blog_link()
        self.nm.click_contact_link()
        self.sc = SubmitContact(self.driver)
        self.sc.set_first_name("Test")
        self.sc.set_last_name("12")
