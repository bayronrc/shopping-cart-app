import flet as ft
from flet_core import MainAxisAlignment

from services import AuthService


class LoginPage(ft.UserControl):
    def __init__(self, page: ft.Page, router=None):
        super().__init__()
        self.page = page
        self.router = router
        self.auth_service = AuthService()

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
            # self.router.navigate("/dashboard")
        else:
            self.error_text.value = message
            self.error_text.color = ft.colors.RED_400

        self.update()

    def build(self):
        return ft.Container(
            content=ft.Column([
                ft.Card(
                    content=ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Text(
                                    "Iniciar Sesión",
                                    size=32,
                                    weight=ft.FontWeight.BOLD,
                                    text_align=ft.TextAlign.CENTER
                                ),
                                self.email_field,
                                self.password_field,
                                self.error_text,
                                ft.ElevatedButton(
                                    text="Iniciar Sesión",
                                    width=300,
                                    on_click=self.handle_login
                                ),
                                ft.Container(
                                    ft.Divider(thickness=2, color=ft.colors.GREY,opacity=0.2),
                                    width=300
                                ),
                                ft.Row(
                                    controls=[
                                        ft.ElevatedButton(
                                            content=ft.Image(
                                                src_base64='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',
                                                height=50,
                                                width=50,
                                            ),
                                            color=ft.colors.WHITE,
                                            width=150
                                        ),
                                        ft.ElevatedButton(
                                            content=ft.Image(
                                                src_base64='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',
                                                height=50,
                                                width=50,

                                            ),
                                            color=ft.colors.WHITE,
                                            width=150
                                        ),
                                    ],
                                    spacing=50,
                                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                    width=300
                                )

                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            spacing=20
                        ),
                        padding=30,
                    )
                )
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER),
            margin=ft.margin.only(top=20)
        )
