from selene import browser, command, have

from qa_quru_puthon_8_10 import resource


class RegistrationPage:

    def open(self):
        browser.open("/automation-practice-form")

    def registration_user(self, user):
        browser.element("#firstName").type(user.first_name)
        browser.element("#lastName").type(user.last_name)
        browser.element("#userEmail").type(user.email)
        browser.element('[for="gender-radio-1"]').click()
        if user.gender == "Male":
            browser.element('[for="gender-radio-1"]').click()
        elif user.gender == "Female":
            browser.element('[for="gender-radio-2"]').click()
        else:
            browser.element('[for="gender-radio-3"]').click()
        browser.element("#userNumber").type(user.phone_number)
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(user.month)
        browser.element('.react-datepicker__year-select').type(user.year)
        browser.element(
            f'.react-datepicker__day--0{user.day}:not(.react-datepicker__day--outside-month)'
        ).click()
        browser.element("#subjectsInput").type(user.subject)
        browser.all(".subjects-auto-complete__menu-list").first.click()
        if user.hobby == "Sports":
            browser.element("[for='hobbies-checkbox-3']").click()
        elif user.hobby == "Reading":
            browser.element("[for='hobbies-checkbox-2']").click()
        elif user.hobby == "Music":
            browser.element("[for='hobbies-checkbox-3']").click()
        browser.element("#uploadPicture").send_keys(resource.path(user.file))
        browser.element("#currentAddress").type(user.current_address)
        browser.element('[id="stateCity-label"]').perform(command.js.scroll_into_view)
        browser.element("#state").click()
        browser.all(".css-11unzgr").element_by(have.text(user.state)).click()
        browser.element("#city").click()
        browser.all(".css-11unzgr").element_by(have.text(user.city)).click()
        browser.element("#submit").click()

    def student_should_by_registred(self, user):
        browser.all(".table-dark>tbody>tr>td:nth-child(2)").should(have.texts(
            f"{user.first_name} {user.last_name}",
            user.email,
            user.gender,
            user.phone_number,
            f"{user.day} {user.month},{user.year}",
            user.subject,
            user.hobby,
            user.file,
            user.current_address,
            f"{user.state} {user.city}"
        ))
