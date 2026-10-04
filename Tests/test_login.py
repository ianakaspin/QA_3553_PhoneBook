from Pages.login_page import LoginPage
from data.user_data import create_user, exiting_user, invalid_email_user, invalid_password_user


def test_login_success(driver):
    login_page = LoginPage(driver)
    user = exiting_user()

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()

    assert login_page.is_logged() is True

def test_login_with_wrong_email(driver):
    login_page = LoginPage(driver)
    user = invalid_email_user()

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()

    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()


def test_login_with_wrong_password(driver):
    login_page = LoginPage(driver)
    user = invalid_password_user()

    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()

    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()


def test_login_unregistered_user(driver):
    login_page = LoginPage(driver)
    user = create_user()
    
    login_page.open_login_form()
    login_page.fill_email(user.username)
    login_page.fill_password(user.password)
    login_page.submit_login()

    assert login_page.get_alert_text() == "Wrong email or password"
    login_page.accept_alert()