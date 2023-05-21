from werkzeug.security import check_password_hash, generate_password_hash


def generate_hash(passwd):
    passwd_hash = generate_password_hash(passwd)
    return passwd_hash


def verify_passwd(passwd_hash, passwd):
    return check_password_hash(passwd_hash, passwd)
