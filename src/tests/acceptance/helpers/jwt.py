import jwt

from .config import get_test_config
from src.pkg.user.model.user import User, Status, Source, Role
from src.pkg.authentication.service.authentication import user_to_jwt_payload


def jwt_token_admin():
    conf = get_test_config()

    u = User(
        username = "admin",
        email = "admin@chuv.ch",
        firstname = "Admin",
        lastname = "Root",
        status = Status.ACTIVE,
        source = Source.INTERNAL,
        roles = [Role(id='admin')]
    )

    expiration_time = conf.daemon.jwt.expiration_time
    secret = conf.daemon.jwt.secret
    payload = user_to_jwt_payload(u, expiration_time)
    payload["user"] = u.to_dict()

    token = jwt.encode(payload, secret, algorithm="HS256")

    return token