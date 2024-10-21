import flet as ft

def register_page():
    register_form = ft.Column(
        controls=[
            ft.TextField(label="Nombre", width=300),
            ft.TextField(label="Correo electrónico", width=300),
            ft.TextField(label="Contraseña", password=True, width=300),
            ft.ElevatedButton("Registrarse", on_click=lambda e: print("Registrarse")),
        ]
    )
    return ft.Card(content=register_form)
