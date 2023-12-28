import pytest
from selenium import webdriver
from Page_Objets.practice_test_automation import LogIn, NavigateMenu, SubmitContact


class TesCase__01:
    valid_user_name = "studen"
    invalid_user_name = "Student"

    valid_password = "Password123"
    invalid_password = "password123"

    url = "https://practicetestautomation.com/practice-test-login/"

    def __init__(self,driver):
        self.driver = driver

