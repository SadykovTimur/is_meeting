from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Menu']


class MenuWrapper(ComponentWrapper):
    profile = Button(xpath='//p[text()="Профиль"]')
    exit = Button(xpath='//p[text()="Выйти"]')


class Menu(Component):
    def __get__(self, instance, owner) -> MenuWrapper:
        return MenuWrapper(instance.app, self.find(instance), self._locator)
