from werkzeug.security import check_password_hash, generate_password_hash


def generate_hash(password:str) -> str:
    password_hash = generate_password_hash(password)
    return password_hash


def verify_passwd(password_hash:str, password:str) -> bool:
    return check_password_hash(password_hash, password)
