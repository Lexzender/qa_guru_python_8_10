from selene import have

from qa_quru_puthon_8_10.pages.registration_page import RegistrationPage


def test_Positive_Student_Registration_Form():
    registration_page = RegistrationPage()

    # WHEN
    registration_page.open()
    registration_page.type_first_name("Aleksei")
    registration_page.type_last_name("Kostromin")
    registration_page.type_email("test@mail.ru")
    registration_page.set_gender("Male")
    registration_page.type_mobile("8927761453")
    registration_page.fill_birthday("1994", "May", "20")
    registration_page.type_subjects("Com")
    registration_page.set_hobbies("Music")
    registration_page.file_upload("file/test.txt")
    registration_page.type_current_address("some text")
    registration_page.scroll_down()
    registration_page.set_state_and_city("Haryana", "Panipat")
    registration_page.submit()

    # THEN
    registration_page.title_should_have_text("Thanks for submitting the form")
    registration_page.registered_user_data.should(have.texts(
        'Aleksei Kostromin',
        'test@mail.ru',
        'Male',
        '8927761453',
        '20 May,1994',
        'Computer Science',
        'Music',
        'test.txt',
        'some text',
        'Haryana Panipat'
    ))
