from datetime import datetime

from src.pkg.user.model.user import User, Status, Source
from server_template.models import TemplatebackendUser


def user_to_business(user: TemplatebackendUser) -> User:
    u = User(
        tenantid=user.tenantid,
        username = user.username,
        email = user.email,
        password = user.password,
        firstname = user.first_name,
        lastname = user.last_name,
        status = Status.ACTIVE,
        source = Source.INTERNAL,
    )

    return u

def user_from_business(user: User) -> TemplatebackendUser:
    print(user)
    u = TemplatebackendUser(
        id=user.id,
        tenantid=user.tenantid,
        username = user.username,
        email = user.email,
        first_name = user.firstname,
        last_name = user.lastname,
        status = user.status,
        #source = user.source,
        roles = [r.id for r in user.roles],
        totp_enabled=(user.totpsecret != ""),
        created_at=user.createdat,
        updated_at=user.updatedat,
    )

    return u
