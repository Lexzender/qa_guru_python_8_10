from qa_quru_puthon_8_10.application import app
from qa_quru_puthon_8_10.data.users import test_user

def test_registers_user():
    app.simple_registration.open()

    app.simple_registration.registration_user(test_user)

    app.simple_registration.student_should_by_registred(test_user)