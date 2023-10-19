from qa_quru_puthon_8_10.data.users import test_user
from qa_quru_puthon_8_10.pages.registration_page import RegistrationPage


def test_Positive_Student_Registration_Form():
    registration_page = RegistrationPage()

    # WHEN
    registration_page.open()
    registration_page.registration_user(test_user)

    # THEN

    registration_page.student_should_by_registred(test_user)
