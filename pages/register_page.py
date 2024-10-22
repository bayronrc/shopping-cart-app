
import flet as ft
from flet_core.alignment import bottom_right


class RegisterPage:
    def __init__(self, page: ft.Page,router = None):
        super().__init__()
        self.page = page
        self.router = router

        self.username_field = ft.TextField(
            label = "Usuario",
            width = 300,
            border_color= ft.colors.BLUE_400
        )
        self.password_field = ft.TextField(
            label = "Contraseña",
            width = 300,
            border_color= ft.colors.BLUE_400,
            password=True,
            can_reveal_password=True
        )
        self.confirm_password_field = ft.TextField(
            label = "Confirmar Contraseña",
            width = 300,
            border_color= ft.colors.BLUE_400,
            can_reveal_password=True
        )
        self.email_field = ft.TextField(
            label = "Email",
            width = 300,
            border_color= ft.colors.BLUE_400,
        )
        self.error_text = ft.Text(
            color=ft.colors.RED_400,
            size=12,
            text_align=ft.TextAlign.CENTER
        )
    # def handle_register(self):


    def build(self):
        return ft.Container(
            content=ft.Column([
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    "Sing Up",
                                    size=32,
                                    weight=ft.FontWeight.BOLD,
                                    text_align=ft.TextAlign.CENTER
                                ),
                                self.username_field,
                                self.email_field,
                                self.password_field,
                                self.confirm_password_field,
                                self.error_text,
                                ft.ElevatedButton(
                                    text="Iniciar Sesión",
                                    width=300,
                                )
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=20
                        ),
                        padding=30,
                    )
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            margin=ft.margin.only(top=50)
        )

