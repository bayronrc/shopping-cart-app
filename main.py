# main.py
import flet as ft

from pages import LoginPage
from router.router import Router
from services import AuthService
from utils import AppConfig

async def main(page: ft.Page):

    page.title = AppConfig.APP_NAME
    page.padding = 0
    page.window_width = 1200
    page.window_height = 800
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.DARK

    auth_service = AuthService()
    router = Router(page,auth_service)

    router.add_route("/login",LoginPage,requires_auth=False)

    router.navigate("/login")
    page.update()


if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)