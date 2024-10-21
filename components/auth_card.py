import flet as ft

class AuthCard(ft.UserControl):
    def __init__(self, title, content, image_url=None, on_click=None):
        super().__init__()
        self.title = title
        self.content = content
        self.image_url = image_url
        self.on_click = on_click

    def build(self):
        # Crear los elementos de la card
        title = ft.Text(self.title, weight="bold", size=16)
        content = ft.Text(self.content)
        
        # Crear la lista de elementos para la card
        card_content = [title, content]
        
        # Añadir imagen si se proporciona una URL
        if self.image_url:
            image = ft.Image(
                src=self.image_url,
                width=200,
                height=200,
                fit=ft.ImageFit.CONTAIN,
            )
            card_content.insert(0, image)
        
        # Crear la card
        card = ft.Card(
            content=ft.Container(
                content=ft.Column(card_content, spacing=10),
                padding=10,
                expand=True
            ),
            elevation=5,
            on_click=self.on_click
        )
        
        return card