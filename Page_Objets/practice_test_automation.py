from selenium.webdriver.common.by import By


class LogIn:
    def __init__(self, driver):
        self.driver = driver

        self.set_user_name = (By.ID, "username")
        self.set_pass_word = (By.ID, "password")
        self.click_login_button = (By.ID, "submit")

    def set_username(self, username):
        self.driver.find_element(*self.set_user_name).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(*self.set_pass_word).send_keys(password)

    def click_submit_button(self):
        self.driver.find_element(*self.click_login_button).click()


class NavigateMenu:
    def __init__(self, driver):
        self.driver = driver

        self.click_home = (By.XPATH, "//li[@id='menu-item-43']//a[1]")
        self.click_practice = (By.XPATH, "//li[@id='menu-item-20']//a[1]")
        self.click_course = (By.XPATH, "(//li[contains(@class,'menu-item menu-item-type-post_type')]//a)[3]")
        self.click_blog = (By.XPATH, "//li[@id='menu-item-19']//a[1]")
        self.click_contact = (By.XPATH, "//li[@id='menu-item-18']//a[1]")

    def click_home_link(self):
        self.driver.find_element(*self.click_home).click()

    def click_practice_link(self):
        self.driver.find_element(*self.click_practice).click()

    def click_courses_link(self):
        self.driver.find_element(*self.click_course).click()

    def click_blog_link(self):
        self.driver.find_element(*self.click_blog).click()

    def click_contact_link(self):
        self.driver.find_element(*self.click_contact).click()


class SubmitContactInfo:
    def __init__(self, driver):
        self.driver = driver

        self.set_firstname = (By.NAME, "wpforms[fields][0][first]")
        self.set_lastname = (By.NAME, "wpforms[fields][0][last]")
        self.set_email = (By.NAME, "wpforms[fields][1]")
        self.comment_message = (By.NAME, "wpforms[fields][2]")
        self.click_submit = (By.NAME, "wpforms[submit]")

    def set_first_name(self, firstname):
        self.driver.find_element(*self.set_firstname).send_keys(firstname)

    def set_last_name(self, lastname):
        self.driver.find_element(*self.set_lastname).send_keys(lastname)

    def set_mail(self, email):
        self.driver.find_element(*self.set_email).send_keys(email)

    def click_submitbutton(self):
        self.driver.find_element(*self.click_submit).click()
