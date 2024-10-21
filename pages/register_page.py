import flet as ft


class RegisterPage(ft.View):
    def __init__(self, page, auth_state, on_login_success):
        super().__init__()
        self.page = page
        self.auth_state = auth_state
        self.on_login_success = on_login_success
