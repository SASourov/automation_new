from selenium import webdriver
import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.keys import Keys

last_name = random.randint(0, 99)
phn_number = random.randint(00000000, 99999999)

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demo.automationtesting.in/Register.html")


def register_from():
    set_frst_name = driver.find_element(By.XPATH, "//div[contains(@class,'col-md-4 col-xs-4')]//input")
    set_frst_name.clear()
    set_frst_name.send_keys("Test")

    set_last_name = driver.find_element(By.XPATH, "(//div[contains(@class,'col-md-4 col-xs-4')]//input)[2]")
    set_last_name.clear()
    set_last_name.send_keys(last_name)

    set_address = driver.find_element(By.XPATH, "//div[contains(@class,'col-md-8 col-xs-8')]//textarea[1]")
    set_address.clear()
    set_address.send_keys("AddressAddressAddressAddressAddressAddressAddressAddressAddress", str(last_name))

    set_email = driver.find_element(By.XPATH, "//div[@id='eid']//input[1]")
    set_email.clear()
    set_email.send_keys("test", str(last_name), "@mail.com")

    set_phone_number = driver.find_element(By.XPATH, "//input[@type='tel']")
    set_phone_number.clear()
    set_phone_number.send_keys("017", str(phn_number))

    select_gender = driver.find_element(By.XPATH, "//input[@name='radiooptions']")
    select_gender.click()

    set_hobbies = driver.find_element(By.XPATH, "//input[@type='checkbox']")
    set_hobbies.click()

    # set_language = Select(driver.find_element(By.ID, "msdd"))
    # set_language.select_by_value("")

    select_skills = Select(driver.find_element(By.XPATH, "//select[@ng-model='Skill']"))
    select_skills.select_by_value("Python")

    select_country = driver.find_element(By.XPATH, "//select[@ng-model='country']")
    select_country.send_keys("Aus", Keys.ENTER)

    set_birth_year = Select(driver.find_element(By.XPATH, "//select[@ng-model='yearbox']"))
    set_birth_year.select_by_value("1995")

    set_birth_month = Select(driver.find_element(By.XPATH, "(//div[contains(@class,'col-md-3 col-xs-3')]//select)[2]"))
    set_birth_month.select_by_value("May")

    set_birth_date = Select(driver.find_element(By.XPATH, "//select[@placeholder='Day']"))
    set_birth_date.select_by_value("10")

    set_password = driver.find_element(By.ID, "firstpassword")
    set_password.send_keys("1230105")

    set_confirm_password = driver.find_element(By.ID, "secondpassword")
    set_confirm_password.send_keys("1230105")

    upload_photo = driver.find_element(By.ID, "imagesrc")
    upload_photo.send_keys(r"E:\Document for Upload\Photos\1869679.png")

    click_submit_button = driver.find_element(By.ID, "submitbtn")
    click_submit_button.click()

    time.sleep(10)


register_from()
driver.quit()
print("***************Hello, Mr. Reviewer. Thanks a lot for review this code.***************")