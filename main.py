import flet as ft
from pages.login_page import LoginPage
from components.auth_state import AuthState


def main(page: ft.Page):
    page.title = "Shopping Cart App"
    auth_state = AuthState()

    def route_change(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(LoginPage(page, auth_state, on_login_success))
        # if page.route == "/register":
        #     page.views.append(RegisterPage(page, auth_state, on_register_success))
        # if page.route == "/home":
        #     page.views.append(HomePage(page, auth_state, on_logout))
        else:
            page.go("/")

        page.update()

    def on_login_success():
        page.go("/home")

    def on_register_success():
        page.go("/home")

    def on_logout():
        auth_state.clear()
        page.go("/")

    page.on_route_change = route_change
    page.go(page.route)


ft.app(target=main)
