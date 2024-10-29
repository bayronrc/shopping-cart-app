# main.py
import flet as ft

from router.router import Router
from utils import AppConfig


def main(page: ft.Page):
    page.title = AppConfig.APP_NAME
    page.padding = 0
    page.window_width = 1200
    page.window_height = 800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.Theme(color_scheme_seed="green")

    router = Router(page)

    page.on_route_change = lambda e: router.navigate(page.route)

    page.go("/login")




if __name__ == "__main__":
    ft.app(target=main, view=ft.AppView.WEB_BROWSER)
