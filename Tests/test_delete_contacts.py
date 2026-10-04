from Pages.contacts_page import ContactsPage
import logging

logger = logging.getLogger(__name__)

def test_delete_contact_decreases_list_by_one(ensure_min_contacts):
    logger.info("Test: delete first contact")

    contacts_page = ContactsPage(ensure_min_contacts)

    contacts_page.open_contacts_list()
    count_before = contacts_page.total_contacts_count()

    logger.info(f"Contacts before delete: {count_before}")

    contacts_page.open_first_contact()
    contacts_page.remove_current_contact()
    count_after = contacts_page.total_contacts_count()

    logger.info(f"Contacts after delete: {count_after}")

    assert count_after == count_before-1

def test_remove_all_contacts(ensure_min_contacts):
    contacts_page = ContactsPage(ensure_min_contacts)

    contacts_page.open_contacts_list()
    contacts_page.remove_all_contacts()
    assert contacts_page.total_contacts_count() == 0
