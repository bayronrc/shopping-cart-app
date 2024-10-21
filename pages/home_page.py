import flet as ft

class HomePage(ft.View):
    def __init__(self, page, auth_state, on_logout):
        super().__init__()
        self.page = page
        self.auth_state = auth_state
        self.on_logout = on_logout
        self.controls = [
            ft.AppBar(title=ft.Text("Página principal")),
            ft.Text(f"Bienvenido, {self.auth_state.username}!"),
            ft.ElevatedButton("Cerrar sesión", on_click=self.logout),
        ]

    def logout(self, e):
        self.on_logout()