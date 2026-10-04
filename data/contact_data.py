# тест должен не сам готовить тестовые данные, а запрашивать их.
# поэтому создается папка data, в которой хранятся фабрики тестовых данных - ф-и, которые создают, напр., контакты

from faker import Faker

from models.contact import Contact

fake = Faker()

def create_contact(name=None, last_name=None, phone=None, email=None, address=None, description=None):
    return Contact(
        name = name if name is not None else fake.first_name(),
        last_name = last_name if last_name is not None else fake.last_name(),
        email = email if email is not None else fake.unique.email(),
        phone = phone if phone is not None else fake.numerify("05########"),
        address = address if address is not None else fake.street_address(),
        description = description if description is not None else fake.sentence(nb_words=5)
    )




#для негативных тестов, в к-рых всё валидно, кроме 1 поля, будем создавать то поле, к-рое хотим изменить. Остальные поля будут случайными

# def create_contact(**overrides) -> Contact: вариант ф-и, к-рая принимает неогр.кол-во именных параметров, к-рые можно поменять
#     data = {
#         "name": fake.first_name(),
#         "last_name": fake.last_name(),
#         "email": fake.unique.email(),
#         "phone": fake.numerify("05########"),
#         "address": fake.street_address(),
#         "description": fake.sentence(), }
#     data.update(overrides)
#     return Contact(**data)