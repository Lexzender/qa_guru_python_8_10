from qa_quru_puthon_8_10.pages.SimpleUserRegistrationPage import SimpleUserRegistrationPage
from qa_quru_puthon_8_10.pages.registration_page import RegistrationPage


class Application:
    def __init__(self):
        self.simple_registration = SimpleUserRegistrationPage()
        self.registration = RegistrationPage()

app = Application()