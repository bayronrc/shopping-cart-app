import flet as ft
class Router:
    def __init__(self,page: ft.Page, auth_service):
        self.page = page
        self.routes = {}
        self.auth_service = auth_service

    def add_route(self, route:str, view_class, requires_auth:bool = False):
        self.routes[route] = {
            "view_class" : view_class,
            "requires_auth" : requires_auth
        }

    def navigate(self, route:str):
        if route not in self.routes:
            print(f"Route {route} not found ")
            return
        route_config = self.routes[route]

        self.page.controls.clear()
        view = route_config["view_class"](self.page,self)
        self.page.controls.append(view)
        self.page.update()