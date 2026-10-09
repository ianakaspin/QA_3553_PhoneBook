import pytest

from data.user_data import invalid_email_user, invalid_password_user, create_user

INVALID_LOGIN_USERS = [
    pytest.param(invalid_email_user,id = "invalid_email"),
    pytest.param(invalid_password_user, id = "invalid_password"),
    pytest.param(create_user, id = "unregistered_user")
]

INVALID_REGISTRATION_USERS = [
    pytest.param(invalid_email_user, id="invalid-email"),
    pytest.param(invalid_password_user, id="invalid-password"),
]