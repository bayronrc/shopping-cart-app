import flet as ft

class AuthService:
    def login(self, email, password):

        if email == "user@example.com" and password == "password123":
            return True, "¡Login exitoso!"
        else:
            return False, "Credenciales incorrectas"


class LoginPage(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
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
            # Aquí puedes agregar la lógica para redirigir a la página de dashboard
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
                                                src='assets/google_icon.png',
                                                height=50,
                                                width=50,
                                            ),
                                            color=ft.colors.WHITE,
                                            width=250
                                        ),
                                        ft.ElevatedButton(
                                            width=200,
                                            content=ft.Row(
                                                [
                                                    ft.Image(src='assets/google_icon.png', height=50, width=50),
                                                    ft.Text("Iniciar sesion con Google")
                                                ]
                                            )
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
