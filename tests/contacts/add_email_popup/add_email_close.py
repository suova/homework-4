from steps.auth.auth_steps import AuthSteps
from steps.contacts.contacts_steps import ContactsSteps
from tests.base_test import BaseTest


class AddPopupEmailCloseTest(BaseTest):

    def test(self):
        AuthSteps(self.driver).auth()
        ContactsSteps(self.driver).add_email_popup_close()