import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By

random_number = random.randint(0, 999)
base_url = "https://practicetestautomation.com/practice-test-login/"
valid_username = "student"
valid_password = "Password123"
invalid_username = "Teacher"
invalid_password = "Password111"
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)


def invalid_login():
    driver.get(base_url)
    set_user_name = driver.find_element(By.ID, "username")
    set_user_name.clear()
    set_user_name.send_keys(invalid_username)

    set_user_password = driver.find_element(By.ID, "password")
    set_user_password.clear()
    set_user_password.send_keys(invalid_password)

    click_login_button = driver.find_element(By.ID, "submit")
    click_login_button.click()
    time.sleep(2)

    expected_txt = driver.find_element(By.ID, "error").text
    if expected_txt == "Your username is invalid!":
        print("Test Passed, Your Expected Text is :", expected_txt)
        assert True
    else:
        print("Test Failed, Your Expected Text is :", expected_txt)
        assert False

    print("*************InValid Test Done*************\n \n")


def without_user_login():
    driver.get(base_url)
    set_user_name = driver.find_element(By.ID, "username")
    set_user_name.clear()
    set_user_name.send_keys("")

    set_user_password = driver.find_element(By.ID, "password")
    set_user_password.clear()
    set_user_password.send_keys("")

    click_login_button = driver.find_element(By.ID, "submit")
    click_login_button.click()
    time.sleep(2)

    expected_txt = driver.find_element(By.ID, "error").text
    if expected_txt == "Your username is invalid!":
        print("Test Passed, Your Expected Text is :", expected_txt)
        assert True
    else:
        print("Test Failed, Your Expected Text is :", expected_txt)
        assert False

    print("*************Without Credential Test Done*************\n \n")


def valid_login():
    driver.get(base_url)
    set_user_name = driver.find_element(By.ID, "username")
    set_user_name.clear()
    set_user_name.send_keys(valid_username)

    set_user_password = driver.find_element(By.ID, "password")
    set_user_password.clear()
    set_user_password.send_keys(valid_password)

    click_login_button = driver.find_element(By.ID, "submit")
    click_login_button.click()
    time.sleep(2)
    driver.refresh()

    expected_title = driver.title
    if expected_title == "Logged In Successfully | Practice Test Automation":
        print("Test Passed, Your Expected Text is :", expected_title)
        assert True
    else:
        print("Test Failed, Your Expected Text is :", expected_title)
        assert False

    print("*************Valid Test Done*************\n \n")


def navigate_menu():
    driver.get(base_url)

    menu_home = driver.find_element(By.XPATH, "//li[@id='menu-item-43']//a[1]")
    menu_home.click()
    time.sleep(2)

    menu_practice = driver.find_element(By.XPATH, "//li[@id='menu-item-20']//a[1]")
    menu_practice.click()
    time.sleep(2)

    menu_courses = driver.find_element(By.XPATH, "//li[@id='menu-item-21']//a[1]")
    menu_courses.click()
    time.sleep(2)

    menu_blogs = driver.find_element(By.XPATH, "//li[@id='menu-item-19']//a[1]")
    menu_blogs.click()
    time.sleep(2)

    click_contact_menu = driver.find_element(By.XPATH, "//li[@id='menu-item-18']//a[1]")
    click_contact_menu.click()

    expected_title = driver.title

    if expected_title == "Contact | Practice Test Automation | Selenium WebDriver":
        print("Test Passed. Your Expected Text is : ", expected_title)
        assert True

    else:
        print("Test Failed. Your Expected Text is : ", expected_title)
        assert False

    print("*************Menu Navigate  Test Done**************\n\n")


invalid_login()
without_user_login()
valid_login()
navigate_menu()
driver.quit()
