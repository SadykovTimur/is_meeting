from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.main_page.components.header import Header
from dit.qa.pages.main_page.components.menu import Menu

__all__ = ['MainPage']


class MainPage(Page):
    header = Header(tag='header')
    menu = Text(tag='aside')
    search = Component(xpath='//label[text()="Название встречи"]')
    create = Component(xpath='//span[text()="Создать встречу"]')
    plan = Component(xpath='//span[text()="Запланировать встречу"]')
    planned_meet = Component(xpath='//h3[text()="Планируемые конференции"]')
    past_meet = Component(xpath='//h3[text()="Прошедшие конференции"]')
    menu_popover = Menu(css='[id*="popovercontent"]')

    def logout(self) -> None:
        self.app.move_to_element(self.header.menu.webelement)
        self.menu_popover.exit.click()

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.header.hide.visible
                assert self.header.menu.visible
                assert "Переговорка" in self.menu
                assert self.search.visible
                assert self.create.visible
                assert self.plan.visible
                assert self.planned_meet.visible

                return self.past_meet.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, msg='Page was not loaded')
        self.app.restore_implicitly_wait()
