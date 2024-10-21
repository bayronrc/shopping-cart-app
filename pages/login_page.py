import flet as ft
from components.auth_card import AuthCard
from models.user import User, users

class LoginPage(ft.View):
    def __init__(self, page, auth_state, on_login_success):
        super().__init__()
        self.page = page
        self.auth_state = auth_state
        self.on_login_success = on_login_success
        self.controls = AuthCard(self.page, self.auth_state)

    def login(self, e):
        user = next((u for u in users if u.username == self.username.value and u.password == self.password.value), None)
        if user:
            self.auth_state.set_auth(user.username)
            self.on_login_success()
        else:
            self.page.snack_bar = ft.SnackBar(ft.Text("Usuario o contraseña incorrectos"))
            self.page.snack_bar.open = True
            self.page.update()