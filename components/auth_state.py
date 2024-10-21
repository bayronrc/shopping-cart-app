class AuthState:
    def __init__(self):
        self._username = ""

    def set_auth(self, username):
        self._username = username

    def clear(self):
        self._username = ""

    @property
    def is_authenticated(self):
        return bool(self._username)

    @property
    def username(self):
        return self._username