from _pytest import logging
import pytest

from Pages.login_page import LoginPage
from data.user_data import create_user, existing_user, invalid_email_user, invalid_password_user
from data.user_datasets import INVALID_LOGIN_USERS
from pages.login_page import LoginPage

logger = logging.getLogger(__name__)

@pytest.mark.smoke
@pytest.mark.regression
@allure.feature("Login")
@allure.story("Login success")
@allure.title("Logging of user with valid data")
@allure.description("User with valid data log in the system. Fill fields email and password and click on button [login] ")
@allure.severity(allure.severity_level.CRITICAL)
def test_login_success(driver):
    login_page = LoginPage(driver)
    user = existing_user()

    logger.info("Testing successful login: username=%s", user.username)

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()

    assert login_page.is_logged() is True

@pytest.mark.regression
@pytest.mark.parametrize("user_factory",INVALID_LOGIN_USERS)
@allure.title("Logging of user with invalid data")
def test_login_rejected(driver,user_factory):
    login_page = LoginPage(driver)
    user = user_factory()

    logger.info("Testing rejected login: case = %s, username=%s",
                user_factory.__name__,
                user.username)

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()

    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()

# def test_login_with_wrong_email(driver):
#     login_page = LoginPage(driver)
#     user = invalid_email_user()
#
#     login_page.open_login_form()
#     login_page.fill_email(user.username)
#     login_page.fill_password(user.password)
#     login_page.submit_login()
#
#     assert login_page.get_alert_text() == "Wrong email or password"
#     login_page.accept_alert()
#
#
# def test_login_with_wrong_password(driver):
#     login_page = LoginPage(driver)
#     user = invalid_password_user()
#
#     login_page.open_login_form()
#     login_page.fill_email(user.username)
#     login_page.fill_password(user.password)
#     login_page.submit_login()
#
#     assert login_page.get_alert_text() == "Wrong email or password"
#     login_page.accept_alert()
#
#
# def test_login_unregistered_user(driver):
#     login_page = LoginPage(driver)
#     user = create_user()
#
#     login_page.open_login_form()
#     login_page.fill_email(user.username)
#     login_page.fill_password(user.password)
#     login_page.submit_login()
#
#     assert login_page.get_alert_text() == "Wrong email or password"
#     login_page.accept_alert()