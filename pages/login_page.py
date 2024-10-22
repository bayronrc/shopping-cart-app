import flet as ft

from services import AuthService


class LoginPage(ft.UserControl):
    def __init__(self, page: ft.Page,router = None):
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
