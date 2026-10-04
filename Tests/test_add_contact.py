import random
import logging
import pytest
import time

from Pages.add_contact_page import ContactPage
from Pages.contacts_page import ContactsPage
from data.contact_data import create_contact
from models.contact import Contact
from faker import Faker
import inspect

fake = Faker()
logger = logging.getLogger(__name__)

def test_add_contact_success_all_fields(authenticated_driver):
    logger.info("Test: test_add_contact_success_all_fields")
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact()

    contact_page.create_contact(contact)

    assert contacts_page.contact_card_visible(contact.phone)

def test_add_contact_success_req_fields(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact(description="")

    contact_page.create_contact(contact)

    assert contacts_page.contact_card_visible(contact.phone)

PHONE_ALERT_TEXT = "Phone not valid: Phone number must contain only digits! And length min 10, max 15!"
EMAIL_ALERT_TEXT = "Email not valid: должно иметь формат адреса электронной почты"

def test_add_contact_empty_name(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(name="")

    contact_page.create_contact(contact)

    assert contact_page.is_add_button_active()

    contacts_page.open_contacts_list()
    assert contacts_page.contact_cards_count(contact.phone) == 0

def test_add_contact_empty_last_name(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(last_name="")

    contact_page.create_contact(contact)

    assert contact_page.is_add_button_active()
    contacts_page.open_contacts_list()
    assert contacts_page.contact_cards_count(contact.phone) == 0

#@pytest.mark.skip(reason = "BUG-123: Contact with empty email") - пропускает тест
@pytest.mark.xfail(reason = "BUG-123: Contact with empty email") #ожидаемое падение при баге системы, о к-ром известно. Если функ-сть починят, он начнет проходить

def test_add_contact_empty_email(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(email="")

    contact_page.create_contact(contact)

    assert contact_page.is_add_button_active()
    contacts_page.open_contacts_list()
    assert contacts_page.contact_cards_count(contact.phone) == 0

def test_add_contact_empty_address(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(address="")

    contact_page.create_contact(contact)

    assert contact_page.is_add_button_active()
    contacts_page.open_contacts_list()
    assert contacts_page.contact_cards_count(contact.phone) == 0

def test_add_contact_invalid_phone(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(phone="2134")

    contact_page.create_contact(contact)

    assert contact_page.get_alert_text().strip() == PHONE_ALERT_TEXT
    contact_page.accept_alert()

    assert contact_page.is_add_button_active()

    contacts_page.open_contacts_list()
    assert contacts_page.contact_cards_count(contact.phone) == 0

def test_add_contact_invalid_email(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(email="invalid_email_format")

    contact_page.create_contact(contact)

    assert contact_page.get_alert_text().strip() == EMAIL_ALERT_TEXT
    time.sleep(5)
    contact_page.accept_alert()

    assert contact_page.is_add_button_active()
    contacts_page.open_contacts_list()
    assert contacts_page.contact_cards_count(contact.phone) == 0

@pytest.mark.xfail(reason = "BUG=124: Duplicate phone")
def test_add_contact_duplicate_phone_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)
    contact = create_contact(phone="2134")
    shared_phone = fake.unique.numerify("050###########")
    first_contact = create_contact(phone = shared_phone)
    second_contact = create_contact(phone = shared_phone)


    contact_page.create_contact(first_contact)
    assert contacts_page.contact_card_visible(shared_phone)

    contact_page.create_contact(second_contact)

    contacts_page.open_contacts_list()
    assert contacts_page.contact_cards_count(shared_phone) == 1