from selene import browser, have

class SimpleUserRegistrationPage:

    def open(self):
        browser.open("/text-box")

    def registration_user(self, user):
        browser.element("#userName").type(user.first_name)
        browser.element("#userEmail").type(user.email)
        browser.element("#currentAddress").type(user.current_address)
        browser.element("#submit").click()

    def student_should_by_registred(self, user):
        browser.all('#output p').should(have.texts(
            f'Name:{user.first_name}',
            f'Email:{user.email}',
            f'Current Address :{user.current_address}',
        ))