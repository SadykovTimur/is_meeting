from coms.qa.frontend.pages.component import Component, ComponentWrapper
from coms.qa.frontend.pages.component.button import Button

__all__ = ['Header']


class HeaderWrapper(ComponentWrapper):
    hide = Button(css='[class*="button-edge-start"]')
    menu = Button(class_name='mud-menu')


class Header(Component):
    def __get__(self, instance, owner) -> HeaderWrapper:
        return HeaderWrapper(instance.app, self.find(instance), self._locator)
