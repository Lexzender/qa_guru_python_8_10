import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    month: str
    year: str
    day: str
    subject: str
    hobby: str
    file: str
    current_address: str
    state: str
    city: str


test_user = User(first_name='Aleksei', last_name='Kostromin', email='test@mail.ru', gender='Male',
                 phone_number='8927761453',
                 month='May', year='1994', day='20', subject='Computer Science',
                 hobby='Music', file='test.txt', current_address='some text', state='Haryana',
                 city='Panipat')
