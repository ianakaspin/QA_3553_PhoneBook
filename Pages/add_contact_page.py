from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class ContactPage:
    ADD_NAV_LINK = (By.CSS_SELECTOR,"[href='/add']")
    NAME_INPUT = (By.CSS_SELECTOR,"input[placeholder='Name']")
    LAST_NAME_INPUT = (By.CSS_SELECTOR,"input[placeholder='Last Name']")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[placeholder='Phone']")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[placeholder='email']")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "input[placeholder='Address']")
    DESCRIPTION_INPUT = (By.CSS_SELECTOR, "input[placeholder='description']")
    SAVE_BTN = (By.XPATH,"//button[b[text()='Save']]")

    def __init__(self,driver):
        self.driver = driver

    # def open_contact_form(self):
    #     self.driver.find_element(*self.ADD_NAV_LINK).click()

    def open_contact_form(self):
        print(self.driver.current_url)
        print(self.driver.page_source[:500])
        self.driver.find_element(*self.ADD_NAV_LINK).click()

    def fill_name(self,name):
        self.driver.find_element(*self.NAME_INPUT).clear()
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)

    def fill_last_name(self,last_name):
        self.driver.find_element(*self.LAST_NAME_INPUT).clear()
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name)

    def fill_phone(self,phone):
        self.driver.find_element(*self.PHONE_INPUT).clear()
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)

    def fill_email(self,email):
        self.driver.find_element(*self.EMAIL_INPUT).clear()
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def fill_address(self,address):
        self.driver.find_element(*self.ADDRESS_INPUT).clear()
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)

    def fill_description(self,description):
        self.driver.find_element(*self.DESCRIPTION_INPUT).clear()
        self.driver.find_element(*self.DESCRIPTION_INPUT).send_keys(description)

    def fill_contact_form(self,contact):
        self.fill_name(contact.name)
        self.fill_last_name(contact.last_name)
        self.fill_phone(contact.phone)
        self.fill_email(contact.email)
        self.fill_address(contact.address)
        self.fill_description(contact.description)

    def submit_contact(self):
        self.driver.find_element(*self.SAVE_BTN).click()

    def contact_card_visible(self,phone):
        locator = (By.XPATH,f"//h3[text()='{phone}']")
        element = WebDriverWait(self.driver,10).until(
            EC.presence_of_element_located(locator))
        return element.is_displayed()

    def open_contact_details(self,phone):
        card = self.driver.find_element(By.XPATH,f"//h3[text()='{phone}']/..")
        card.click()

