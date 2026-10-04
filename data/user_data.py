from faker import Faker

from Pages.faker_1 import fake
from models.user import User

faker = Faker()

def create_user(username = None, password = None):
    return User(
        username = username if username is not None else fake.unique.email(),
        password = password if password is not None else fake.password(
            length=12, special_chars=True, digits=True, upper_case=True, lower_case=True)
    )

EXITING_USER_EMAIL = "margo@gmail.com"
EXITING_USER_PASSWORD = "Mmar123456$"
INVALID_EMAIL = "margogmail.com"
INVALID_PASSWORD = "Mmar123"

def exiting_user():
    return create_user(username=EXITING_USER_EMAIL, password=EXITING_USER_PASSWORD)

def invalid_email_user():
    return create_user(username=INVALID_EMAIL, password=EXITING_USER_PASSWORD)

def invalid_password_user():
    return create_user(username=EXITING_USER_EMAIL, password=INVALID_PASSWORD)