from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.auth_page.components.header import Header

__all__ = ['StartPage']


class StartPage(Page):
    header = Header(tag='header')
    menu = Text(tag='aside')
    search = Component(xpath='//label[text()="Идентификатор встречи"]')
    connect = Component(xpath='//span[text()="Присоединиться"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.hide.visible
                assert self.header.login.visible
                assert "Переговорка" in self.menu
                assert self.search.visible

                return self.connect.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
