from src.extensions.database import database
from src.resources.authentication.models.user import User
from src.resources.authentication.services import security_service


def create_user(email: str, password: str):
    user_exist = check_if_user_exists(email)

    if not user_exist:
        password_hash = security_service.generate_hash(password)

        user = User(email=email, password_hash=password_hash)

        database.session.add(user)
        database.session.commit()


def check_if_user_exists(email):
    user = User.query.filter_by(email=email).first()
    if user:
        return True
    else:
        return False


def check_user_credentials(email: str, password: str) -> bool:
    user = User.query.filter_by(email=email).first()
    return security_service.check_password_hash(user.password_hash, password)
