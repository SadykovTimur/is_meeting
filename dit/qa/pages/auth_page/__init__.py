from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

__all__ = ['AuthPage']


class AuthPage(Page):
    logo = Component(class_name='system-logo')
    name = Text(class_name='system-name')
    title = Text(class_name='page-title')
    login = TextField(id='login')
    password = TextField(id='password')
    forgot_password = Button(id='recoveryEnter')
    submit = Button(id='bind')
    other_user = Component(id='other-user')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.logo.visible
                assert 'Единая система доступа' == self.name
                assert 'Вход в Портал ВКС Тест' == self.title

                assert self.login.visible

                assert self.password.visible
                assert self.forgot_password.visible

                return self.submit.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
