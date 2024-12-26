from faker import Faker
import random

faker = Faker()

def generate_registration_data():
    name = faker.first_name()
    email = f"{name}{faker.last_name()}{random.randint(1, 25)}{random.randint(100, 999)}@yandex.ru"
    password = faker.password(length=6, special_chars=True, digits=True, upper_case=True, lower_case=True)
    return name, email, password
