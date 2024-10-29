class AuthManager:
    def __init__(self):
        self.is_authenticated = False
        self.user = None

    def login(self, email, password):
        # Aqui se debe consultar el usuario de base de datos el cual esta registrado

        if email == "ejemplo_email" and password == "ejemplo_password":
            self.is_authenticated = True
            self.user = email
            return True
        return False

    def logout(self):
        self.is_authenticated = False
        self.user = None
