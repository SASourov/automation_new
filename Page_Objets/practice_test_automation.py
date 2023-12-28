from selenium.webdriver.common.by import By


class LogIn:
    def __init__(self, driver):
        self.driver = driver

        self.set_username = (By.ID, "username")
        self.set_password = (By.ID, "password")
        self.click_login_button = (By.ID, "submit")

    def set_username(self, username):
        self.driver.find_element(self.set_username).clear()
        self.driver.find_element(self.set_username).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(self.set_password).clear()
        self.driver.find_element(self.set_password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(self.click_login_button).click()


class NavigateMenu:
    def __init__(self, driver):
        self.driver = driver

        self.click_home = (By.XPATH, "//li[@id='menu-item-43']//a[1]")
        self.click_practice = (By.XPATH, "//li[@id='menu-item-20']//a[1]")
        self.click_course = (By.XPATH, "(//li[contains(@class,'menu-item menu-item-type-post_type')]//a)[3]")
        self.click_blog = (By.XPATH, "//li[@id='menu-item-19']//a[1]")
        self.click_contact = (By.XPATH, "//li[@id='menu-item-18']//a[1]")

    def click_home_link(self):
        self.driver.find_element(self.click_home).click()

    def click_practice_link(self):
        self.driver.find_element(self.click_practice).click()

    def click_courses_link(self):
        self.driver.find_element(self.click_course).click()

    def click_blog_link(self):
        self.driver.find_element(self.click_blog).click()

    def click_contact_link(self):
        self.driver.find_element(self.click_contact).click()


class SubmitContact:
    def __init__(self, driver):
        self.driver = driver

        self.first_name = (By.NAME, "wpforms[fields][0][first]")
        self.last_name = (By.NAME, "wpforms[fields][0][last]")
        self.email = (By.NAME, "wpforms[fields][1]")
        self.comment_message = (By.NAME, "wpforms[fields][2]")
        self.robot = (By.CSS_SELECTOR, "#modern-store-modified")
        self.submit = (By.CSS_SELECTOR, ".wpforms-submit")

    def set_first_name(self, f_name):
        self.driver.find_element(self.first_name).clear()
        self.driver.find_element(self.first_name).send_keys(f_name)

    def set_last_name(self, l_name):
        self.driver.find_element(self.last_name).clear()
        self.driver.find_element(self.last_name).send_keys(l_name)

    def set_email(self, email):
        self.driver.find_element(*self.email).clear()
        self.driver.find_element(*self.email).send_keys(email)

    def set_comment_message(self, cmnt):
        self.driver.find_element(self.comment_message).clear()
        self.driver.find_element(self.comment_message).send_keys(cmnt)

    def click_robot_verification(self):
        self.driver.find_element(self.robot).click()

    def click_submit_button(self):
        self.driver.find_element(self.submit).click()