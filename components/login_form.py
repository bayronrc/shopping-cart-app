from flet import *

from utils.validators import validate_email, validate_password


class LoginForm(Control):
    def __init__(self, page: Page, on_login):
        super().__init__()
        self.page = page
        self.on_login = on_login

        self.email_field = TextField(
            label='Email',
            border_color=colors.BLUE_400,
            width=300,
            autofocus=True,
        )
        self.password_field = TextField(
            label='Password',
            border_color=colors.BLUE_400,
            password=True,
            can_reveal_password=True,
            width=300,
        )
        self.error_text = Text(
            color=colors.RED_400,
            size=12
        )

    def validate_form(self) -> bool:
        email_valid, email_error = validate_email(self.email_field.value)

        if not email_valid:
            self.error_text.value = email_error
            self.update()
            return False

        password_valid, password_error = validate_password(self.password_field.value)
        if not password_valid:
            self.error_text.value = password_error
            self.update()
            return False
        return True

    async def on_submit(self, _) -> None:
        if not self.validate_form():
            return

        self.error_text.value = ""
        await self.on_login(self.email_field.value, self.password_field.value)

    def build(self):
        return Column(
            controls=[
                Text(
                    "Bienvenido",
                    size=32,
                    weight=FontWeight.BOLD,
                    text_align=TextAlign.CENTER,
                ),
                Text(
                    "Ingresa a tu cuenta",
                    size=16,
                    color=colors.GREEN_700,
                    text_align= TextAlign.CENTER,
                ),
                Divider(height=20, color=colors.TRANSPARENT),
                self.email_field,
                self.password_field,
                self.error_text,
                ElevatedButton(
                    text="Iniciar Sesion",
                    width=300,
                    on_click = self.on_submit,
                ),
                Row(
                    controls=[
                        Text("¿No tienes una cuenta?"),
                        TextButton("Registrate", on_click=lambda _: self.page.go("/register"))
                    ]
                )
            ]
        )
