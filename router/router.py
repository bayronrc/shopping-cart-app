import flet as ft

from pages import LoginPage
from pages.register_page import RegisterPage

ROUTES = {
    "/login": LoginPage,
    "/register": RegisterPage,
}


class Router:
    def __init__(self, page: ft.Page):
        self.page = page

    def navigate(self, route: str):
        if route in ROUTES:
            self.page.controls.clear()
            view = ROUTES[route](self.page)
            self.page.add(view)
        else:
            self.page.controls.clear()
            self.page.add(ft.Text("404 - Not Found"))
        self.page.update()
