import time

from Pages.add_contact_page import ContactPage
from models.contact import Contact


def test_add_contact_success_all_fields(authenticated_driver):
    contact_page = ContactPage(authenticated_driver)

    contact = Contact(
        "Anna",
        "Test",
        "0252456123",
        "anna-test@gmail.com",
        "Tel Aviv",
        "QA lesson contact"
    )

    contact_page.open_contact_form()
    contact_page.fill_contact_form(contact)
    time.sleep(10)
    contact_page.submit_contact()

    assert contact_page.contact_card_visible(contact.phone)