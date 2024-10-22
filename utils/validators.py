import re


def validate_email(email:str) -> [bool,str]:
    if not email:
        return False,"El email es requerido"

    email_pathern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pathern,email):
        return False,"El email es requerido"

    return True
def validate_password(password:str) -> [bool,str]:
    if not password:
        return False,"El password es requerido"

    if len(password) < 8:
        return False,"La contraseña debe tener al menos 6 caracteres"

    return True