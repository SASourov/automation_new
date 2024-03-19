from selenium.webdriver.common.by import By


class SignUpButton:

    def __init__(self, driver):
        self.driver = driver

        self.click_login_menu = (By.XPATH, "//a[@href='/login']")
        self.name = (By.NAME, "name")
        self.email = (By.XPATH, "(//input[@name='email'])[2]")
        self.click_sign_up_button = (By.XPATH, "(//button[@class='btn btn-default'])[2]")
        self.select_title = (By.XPATH, "//input[@type='radio']")
        self.password = (By.ID, "password")
        self.newsletter = (By.ID, "newsletter")
        self.first_name = (By.ID, "first_name")
        self.last_name = (By.ID, "last_name")
        self.address1 = (By.ID, "address1")
        self.address2 = (By.ID, "address2")
        self.state = (By.ID, "state")
        self.city = (By.ID, "city")
        self.zip_code = (By.ID, "zipcode")
        self.mobile_number = (By.ID, "mobile_number")
        self.click_create_ac = (By.XPATH, "//div[@class='login-form']//button[1]")
        self.continue_button = (By.XPATH, "//a[@class='btn btn-primary']")
        self.delete_account = (By.XPATH, "//a[@href='/delete_account']")

    def click_menu(self):
        self.driver.find_element(*self.click_login_menu).click()

    def set_name(self, name):
        self.driver.find_element(*self.name).send_keys(name)

    def set_mail(self, email):
        self.driver.find_element(*self.email).send_keys(email)

    def click_signup_btn(self):
        self.driver.find_element(*self.click_sign_up_button).click()

    def select_name_title(self):
        self.driver.find_element(*self.select_title).click()

    def set_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def select_newsletter(self):
        self.driver.find_element(*self.newsletter).click()

    def set_first_name(self, f_name):
        self.driver.find_element(*self.first_name).send_keys(f_name)

    def set_last_name(self, l_name):
        self.driver.find_element(*self.last_name).send_keys(l_name)

    def set_address_1(self, address1):
        self.driver.find_element(*self.address1).send_keys(address1)

    def set_address_2(self, address2):
        self.driver.find_element(*self.address2).send_keys(address2)

    def set_state(self, state):
        self.driver.find_element(*self.state).send_keys(state)

    def set_city(self, city):
        self.driver.find_element(*self.city).send_keys(city)

    def set_zip_code(self, zip_code):
        self.driver.find_element(*self.zip_code).send_keys(zip_code)

    def set_mobile_number(self, mobile_number):
        self.driver.find_element(*self.mobile_number).send_keys(mobile_number)

    def click_create_account(self):
        self.driver.find_element(*self.click_create_ac).click()

    def click_continue_button(self):
        self.driver.find_element(*self.continue_button).click()

    def click_delete_account(self):
        self.driver.find_element(*self.delete_account).click()

    def click_continue_btn(self):
        self.driver.find_element(*self.continue_button).click()


class InvalidLogin:
    def __init__(self, driver):
        self.driver = driver

        self.click_login_menu = (By.XPATH, "//a[@href='/login']")
        self.email_address = (By.XPATH, "//input[@name='email']")
        self.password = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@class='btn btn-default']")

    def click_menu(self):
        self.driver.find_element(*self.click_login_menu).click()

    def set_email(self, email):
        self.driver.find_element(*self.email_address).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()


class Logout:
    def __init__(self, driver):
        self.driver = driver

        self.click_login_menu = (By.XPATH, "//a[@href='/login']")
        self.email_address = (By.XPATH, "//input[@name='email']")
        self.password = (By.NAME, "password")
        self.login_button = (By.XPATH, "//button[@class='btn btn-default']")
        self.log_out_button = (By.XPATH, "//a[@href='/logout']")

    def click_menu(self):
        self.driver.find_element(*self.click_login_menu).click()

    def set_email(self, email):
        self.driver.find_element(*self.email_address).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def click_logout_button(self):
        self.driver.find_element(*self.log_out_button).click()


class ExistingMail:
    def __init__(self, driver):
        self.driver = driver

        self.click_login_menu = (By.XPATH, "//a[@href='/login']")
        self.name = (By.NAME, "name")
        self.email = (By.XPATH, "(//input[@name='email'])[2]")
        self.click_sign_up_button = (By.XPATH, "(//button[@class='btn btn-default'])[2]")

    def click_menu(self):
        self.driver.find_element(*self.click_login_menu).click()

    def set_name(self, name):
        self.driver.find_element(*self.name).send_keys(name)

    def set_mail(self, email):
        self.driver.find_element(*self.email).send_keys(email)

    def click_signup_btn(self):
        self.driver.find_element(*self.click_sign_up_button).click()


class ContactUs:
    def __init__(self, driver):
        self.driver = driver

        self.contact_us_menu = (By.XPATH, "//a[@href='/contact_us']")
        self.textbox_name = (By.NAME, "name")
        self.textbox_email = (By.NAME, "email")
        self.textbox_subject = (By.NAME, "subject")
        self.textbox_message = (By.ID, "message")
        self.photo_upload = (By.NAME, "upload_file")
        self.submit_button = (By.NAME, "submit")

    def click_contact_us_menu(self):
        self.driver.find_element(*self.contact_us_menu).click()

    def set_name(self, name):
        self.driver.find_element(*self.textbox_name).send_keys(name)

    def set_email(self, email):
        self.driver.find_element(*self.textbox_email).send_keys(email)

    def set_subject(self, subject):
        self.driver.find_element(*self.textbox_subject).send_keys(subject)

    def set_message(self, message):
        self.driver.find_element(*self.textbox_message).send_keys(message)

    def upload_photo(self, file_name):
        self.driver.find_element(*self.photo_upload).send_keys(file_name)

    def click_submit_button(self):
        self.driver.find_element(*self.submit_button).click()


class NavigateTestcasePage:

    def __init__(self, driver):
        self.driver = driver

        self.test_case_menu = (By.XPATH, "//button[@class='btn btn-success']")

    def click_test_case_menu(self):
        self.driver.find_element(*self.test_case_menu).click()


class ProductButton:
    def __init__(self, driver):
        self.driver = driver

        self.product_button = (By.XPATH, "//a[@href='/products']")
        self.view_product_button = (By.XPATH, "//a[@href='/product_details/1']")

    def click_product_button(self):
        self.driver.find_element(*self.product_button).click()

    def click_view_product_button(self):
        self.driver.find_element(*self.view_product_button).click()


class SearchProduct:
    def __init__(self, driver):
        self.driver = driver

        self.product_button = (By.XPATH, "//a[@href='/products']")
        self.textbox_search_product = (By.ID, "search_product")
        self.search_button = (By.XPATH, "//i[@class='fa fa-search']")

    def click_product_button(self):
        self.driver.find_element(*self.product_button).click()

    def set_search_box(self, search):
        self.driver.find_element(*self.textbox_search_product).send_keys(search)

    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()

