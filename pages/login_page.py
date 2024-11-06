import flet as ft

from components import LoginForm
from services import AuthService


class LoginPage(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.auth_service = AuthService()
        self.content = LoginForm(self.auth_service)

        self.email_field = ft.TextField(
            label="Email",
            border_color=ft.colors.BLUE_400,
            width=300,
            autofocus=True
        )

        self.password_field = ft.TextField(
            label="Contraseña",
            border_color=ft.colors.BLUE_400,
            password=True,
            can_reveal_password=True,
            width=300
        )

        self.error_text = ft.Text(
            color=ft.colors.RED_400,
            size=12,
            text_align=ft.TextAlign.CENTER
        )

    def handle_login(self, e):
        success, message = self.auth_service.login(
            self.email_field.value,
            self.password_field.value
        )

        if success:
            self.error_text.value = ""
            self.error_text.color = ft.colors.GREEN_400
            self.error_text.value = "¡Login exitoso!"
            # Aquí puedes agregar la lógica para redirigir a la página de dashboard
        else:
            self.error_text.value = message
            self.error_text.color = ft.colors.RED_400

        self.update()

    def build(self):
        return ft.Container(
            self.content,
            expand=True,
            padding=ft.padding.symmetric(horizontal=10, vertical=10),
        )
