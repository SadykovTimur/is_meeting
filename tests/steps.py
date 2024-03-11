import allure
from coms.qa.fixtures.application import Application
from coms.qa.frontend.helpers.attach_helper import screenshot_attach
from selenium.common.exceptions import NoSuchElementException

from dit.qa.pages.auth_page import AuthPage
from dit.qa.pages.main_page import MainPage
from dit.qa.pages.start_page import StartPage

__all__ = [
    'open_start_page',
    'open_auth_page',
    'sign_in',
    'open_main_page',
    'logout',
]


def open_start_page(app: Application) -> None:
    with allure.step('Opening Start page'):
        try:
            page = StartPage(app)
            page.open()
            page.wait_for_loading()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise TimeoutError('Start page was not loaded') from e


def open_auth_page(app: Application) -> None:
    with allure.step('Opening Auth page'):
        try:
            StartPage(app).header.login.click()
            AuthPage(app).wait_for_loading()

            screenshot_attach(app, 'auth_page')
        except Exception as e:
            screenshot_attach(app, 'auth_page_error')

            raise TimeoutError('Auth page was not loaded') from e


def sign_in(app: Application, login: str, password: str) -> None:
    with allure.step(f'{login} signing in'):
        try:
            page = AuthPage(app)

            page.login.send_keys(login)
            page.password.send_keys(password)

            screenshot_attach(app, 'auth_data')
        except Exception as e:
            screenshot_attach(app, 'auth_data_error')

            raise NoSuchElementException('Entering data exception') from e

        page.submit.click()


def open_main_page(app: Application) -> None:
    with allure.step('Opening Main page'):
        try:
            MainPage(app).wait_for_loading()

            screenshot_attach(app, 'main_page')
        except Exception as e:
            screenshot_attach(app, 'main_page_error')

            raise TimeoutError('Main page was not loaded') from e


def logout(app: Application) -> None:
    with allure.step('Logging out'):
        try:
            MainPage(app).logout()

            StartPage(app).wait_for_loading()

            screenshot_attach(app, 'start_page')
        except Exception as e:
            screenshot_attach(app, 'start_page_error')

            raise TimeoutError('Start page was not loaded') from e
