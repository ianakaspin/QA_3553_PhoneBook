import pytest
from faker import Faker
import logging

from Pages.add_contact_page import ContactPage
from Pages.contacts_page import ContactsPage
from data.contact_data import create_contact

fake = Faker()
logger = logging.getLogger(__name__)

def test_edit_contact_name_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact(contact)
    new_name = fake.first_name()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_NAME_INPUT,new_name)
    contacts_page.submit_edit()

    assert contacts_page.contact_name_for_phone(contact.phone) == new_name

def test_edit_contact_last_name_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact(contact)
    new_last_name = fake.last_name()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_LAST_NAME_INPUT,new_last_name)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_LAST_NAME_INPUT) == new_last_name


def test_edit_contact_phone_updated(authenticated_driver):
    logger.info("Test: update phone number")

    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact(contact)
    new_phone = fake.unique.numerify("050#########")

    logger.debug(f"Old phone:{contact.phone}")
    logger.debug(f"New phone{new_phone}")

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_PHONE_INPUT,new_phone)
    contacts_page.submit_edit()

    assert contacts_page.contact_card_visible(new_phone)
    assert contacts_page.contact_cards_count(contact.phone) == 0 # ноль означает, что с таким №тлф больше нет контактов

def test_edit_contact_email_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact(contact)
    new_email = fake.unique.email()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_EMAIL_INPUT,new_email)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()


    assert contacts_page.get_edit_contact(contacts_page.EDIT_EMAIL_INPUT) == new_email

def test_edit_contact_address_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact(contact)
    new_address = fake.city()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_ADDRESS_INPUT,new_address)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()


    assert contacts_page.get_edit_contact(contacts_page.EDIT_ADDRESS_INPUT) == new_address

@pytest.mark.skip(reason = "BUG-330: Editing description saves literal string [Object undefined]")
def test_edit_contact_description_updated(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact(contact)
    new_description = fake.sentence()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_DESCRIPTION_INPUT,new_description)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()


    assert contacts_page.get_edit_contact(contacts_page.EDIT_DESCRIPTION_INPUT) == new_description

def test_edit_contact_empty_name_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact(contact)

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_NAME_INPUT,"")
    contacts_page.submit_edit()

    assert contacts_page.contact_name_for_phone(contact.phone) == contact.name

def test_edit_contact_empty_last_name_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact(contact)

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_LAST_NAME_INPUT,"")
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_LAST_NAME_INPUT) == contact.last_name

def test_edit_contact_empty_phone_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact(contact)

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_PHONE_INPUT,"")
    contacts_page.submit_edit()

    assert contacts_page.contact_cards_count(contact.phone) == 1

def test_edit_contact_empty_email_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact(contact)

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_EMAIL_INPUT,"")
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_EMAIL_INPUT) == contact.email

def test_edit_contact_empty_address_rejected(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    contact = create_contact()
    contact_page.create_contact(contact)

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_ADDRESS_INPUT,"")
    contacts_page.submit_edit()

    contacts_page.open_contact_details(contact.phone)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_ADDRESS_INPUT) == contact.address

@pytest.mark.skip
def test_edit_contact_duplicate_phone_negative(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    existing = create_contact()
    other = create_contact()

    contact_page.create_contact(existing)
    contact_page.create_contact(other)

    contacts_page.open_contact_details(other.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_PHONE_INPUT,existing.phone)
    contacts_page.submit_edit()

    assert contacts_page.contact_cards_count(existing.phone) == 1

@pytest.mark.skip
def test_edit_contact_duplicate_email_negative(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)
    contacts_page = ContactsPage(authenticated_driver)

    existing = create_contact()
    other = create_contact()

    contact_page.create_contact(existing)
    contact_page.create_contact(other)

    contacts_page.open_contact_details(other.phone)
    contacts_page.open_edit_mode()
    contacts_page.set_edit_field(contacts_page.EDIT_EMAIL_INPUT,existing.email)
    contacts_page.submit_edit()

    contacts_page.open_contact_details(other)
    contacts_page.open_edit_mode()
    assert contacts_page.get_edit_contact(contacts_page.EDIT_EMAIL_INPUT) == other.email