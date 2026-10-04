import logging
import pytest
from selenium import webdriver

from Pages.add_contact_page import ContactPage
from Pages.contacts_page import ContactsPage
from Pages.login_page import LoginPage
from data.contact_data import create_contact
# from Tests.test_login import VALID_EMAIL, VALID_PASSWORD
from data.user_data import exiting_user
from utils.logger_config import configure_logging

#pytest находит этот conftest перед запуском любых тестов. Здесь хранятся фикстуры и прекондишены.
# Pytest знает, что его нужно запустить перед запуском любого теста

configure_logging() #включается общая конфигурация логгинга до начала тестов
logger = logging.getLogger(__name__)

@pytest.fixture
def driver():
    logger.info("Starting browser session")

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://telranedu.web.app/")

    yield driver
    logger.info("Closing browser session")

    driver.quit()

@pytest.fixture
def authenticated_driver(driver):
    login_page = LoginPage(driver)
    user = exiting_user()

    logger.info(f"Logging in user:{user.username}")

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()

    return driver

@pytest.fixture
def ensure_min_contacts(authenticated_driver):
    contacts_page = ContactsPage(authenticated_driver)
    contact_page = ContactPage(authenticated_driver)

    contacts_page.open_contacts_list()
    count = contacts_page.total_contacts_count()
    if count <3:
        logger.warning(f"Contact list has {count} contacts (<3), creating test data")
    while contacts_page.total_contacts_count()<3:
        contact_page.create_contact(create_contact())
        contacts_page.open_contacts_list()

    return authenticated_driver

